import random
from pathlib import Path
import os
import glob

from flask import Flask, jsonify, render_template, request, url_for
from rdkit import Chem
from rdkit.Chem import Draw
import joblib
from rdkit import Chem
from rdkit.Chem import Descriptors

# 1. Setup Paths
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
STATIC_DIR.mkdir(exist_ok=True)

def cleanup_static():
    """Deletes all structure images from the static folder on startup."""
    files = glob.glob(str(STATIC_DIR / "structure_*.png"))
    for f in files:
        try:
            os.remove(f)
        except Exception as e:
            print(f"Error deleting file {f}: {e}")

# Run the cleanup before the app starts
cleanup_static()

# 3. Load the trained model
saved_data = joblib.load("model/random_forest_model.joblib")
# Extract the actual model and the threshold
model = saved_data['model']
threshold = saved_data.get('optimal_threshold', 0.27)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Accept SMILES from form-data or JSON body.
    smiles = request.form.get("smiles")
    if not smiles and request.is_json:
        data = request.get_json(silent=True) or {}
        smiles = data.get("smiles")

    if not smiles:
        return jsonify({"error": "SMILES string is required"}), 400

    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return jsonify({"error": "Invalid SMILES string"}), 400

    import time
    # 1. Create the filename and save the image
    img_filename = f"structure_{int(time.time())}.png"
    img_path = STATIC_DIR / img_filename
    Draw.MolToFile(mol, str(img_path))

    # Extract molecular descriptors (same as training)
    molecular_weight = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    h_bond_donors = Descriptors.NumHDonors(mol)
    h_bond_acceptors = Descriptors.NumHAcceptors(mol)
    tpsa = Descriptors.TPSA(mol)
    num_atoms = mol.GetNumAtoms()

    # Create feature list (IMPORTANT: same order as training)
    features = [
        molecular_weight,
        logp,
        h_bond_donors,
        h_bond_acceptors,
        tpsa,
        num_atoms
    ]

    # Use the loaded model to make a prediction
    toxicity_score = model.predict_proba([features])[0][1]  # Probability of being toxic
    confidence = int(toxicity_score*100) if toxicity_score >= threshold else int((1 - toxicity_score)*100)

    # Simulated research-based explanation based on descriptors and toxicity score
    size_phrase = (
        "a relatively compact molecular framework"
        if molecular_weight < 280
        else "a more substantial molecular framework"
    )
    hb_phrase = (
        "modest hydrogen-bond donor and acceptor contributions"
        if h_bond_donors + h_bond_acceptors <= 6
        else "notable hydrogen-bond donor and acceptor capacity"
    )

    if toxicity_score < 0.33:
        line1 = (
            f"Taken together, {size_phrase} and {hb_phrase} suggest a profile more often "
            "associated with limited non-specific biological interaction."
        )
    elif toxicity_score <= 0.66:
        line1 = (
            "Based on molecular weight and hydrogen bonding capacity, the compound reflects an intermediate "
            f"profile—{size_phrase} with {hb_phrase}—which can influence solubility, permeability, and the "
            "degree of biological engagement."
        )
    else:
        line1 = (
            "Based on molecular weight and hydrogen bonding capacity, the compound shows "
            "characteristics associated with increased biological interaction."
        )

    line2 = (
        "Such properties are often linked to toxicity patterns observed in chemical and "
        "pharmaceutical studies."
    )
    reason = line1 + "\n\n" + line2

    if toxicity_score > 0.6:
        predefined_safe = {
            "c1ccccc1": "CCO",
            "CCN(CC)CC": "CC(O)C",
            "CC(=O)O": "CCO",
        }
        key = smiles.strip()
        alt_smiles = predefined_safe.get(key)
        if alt_smiles is None:
            alt_smiles = None
            for suffix in ("O", "C"):
                trial_mol = Chem.MolFromSmiles(smiles + suffix)
                if trial_mol is not None:
                    alt_smiles = Chem.MolToSmiles(trial_mol)
                    break
        if alt_smiles is None:
            alt_smiles = random.choice(["CCO", "CC(C)O", "CC(=O)O"])
        suggested_analog = f"Safer alternative to explore (mock): {alt_smiles}"
    else:
        suggested_analog = (
            "Compound appears safe. Similar structures can be explored."
        )

    return jsonify(
        {
            "smiles": smiles,
            "toxicity_score": toxicity_score,
            "confidence": confidence,
            "molecular_weight": molecular_weight,
            "h_bond_donors": h_bond_donors,
            "h_bond_acceptors": h_bond_acceptors,
            "reason": reason,
            "suggested_analog": suggested_analog,
            "structure_image": url_for("static", filename=img_filename),
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
