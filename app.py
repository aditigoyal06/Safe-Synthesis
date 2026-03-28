import random
from pathlib import Path

from flask import Flask, jsonify, render_template, request, url_for
from rdkit import Chem
from rdkit.Chem import Draw

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
STRUCTURE_IMAGE_PATH = STATIC_DIR / "structure.png"


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

    STATIC_DIR.mkdir(exist_ok=True)
    # TODO: Improve image handling (unique filenames, cleanup)
    Draw.MolToFile(mol, str(STRUCTURE_IMAGE_PATH))

    # TODO: Replace mock values with real ML model + RDKit descriptors
    toxicity_score = round(random.uniform(0, 1), 4)
    confidence = random.randint(70, 95)
    molecular_weight = round(random.uniform(100, 500), 2)
    h_bond_donors = random.randint(0, 5)
    h_bond_acceptors = random.randint(0, 10)

    # Simulated research-based explanation (mock)
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

    return jsonify(
        {
            "smiles": smiles,
            "toxicity_score": toxicity_score,
            "confidence": confidence,
            "molecular_weight": molecular_weight,
            "h_bond_donors": h_bond_donors,
            "h_bond_acceptors": h_bond_acceptors,
            "reason": reason,
            "structure_image": url_for("static", filename="structure.png"),
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
