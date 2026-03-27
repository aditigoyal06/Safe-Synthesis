from flask import Flask, jsonify, render_template, request
import random

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

    # TODO: Load real ML model here
    toxicity_score = round(random.uniform(0, 1), 4)

    return jsonify({
        "smiles": smiles,
        "toxicity_score": toxicity_score
    })


if __name__ == "__main__":
    app.run(debug=True)
