#  Safe Synthesis

**Prevention is better than cure — A powered toxicity prediction from SMILES**

---

##  Overview

Safe Synthesis is a machine learning-based web application that predicts the **toxicity of chemical compounds** using their **SMILES (Simplified Molecular Input Line Entry System)** representation.

The system aims to assist researchers, chemists, and students in **early-stage screening of compounds**, helping reduce risks before synthesis or exposure.

---

##  Problem Statement

In chemical and pharmaceutical research:

* Compounds are often synthesized **without early toxicity screening**
* This leads to:

  *  Health risks
  *  Wasted resources
  *  Failed experiments

Additionally, many AI systems act as **black boxes**, providing predictions without explanations.

---

## 💡 Our Solution

Safe Synthesis provides a:

*  **Predictive system** (toxicity detection)
*  **Explainable interface** (descriptor-based reasoning)
*  **User-friendly web app**

---

##  Key Features

###  Core Features

* SMILES → **Structure Image**
* **Toxicity Prediction** using ML model
* **Confidence Score**
* **Molecular Descriptor Analysis**
* **Reason-based Explanation**
* **Alternative Compound Suggestion (Mock)**

---

## 🧪 Machine Learning Pipeline

###  Dataset

* Molecular dataset with:

  * SMILES strings
  * Multiple toxicity endpoints

 Focused on **SR-ARE** (binary toxicity classification)

---

### ⚙️ Preprocessing

* Removed missing target values
* Converted SMILES → molecular structures
* Filtered invalid molecules

---

###  Feature Engineering

Extracted interpretable molecular descriptors:

* Molecular Weight (MolWt)
* LogP (hydrophobicity)
* Hydrogen Bond Donors (HBD)
* Hydrogen Bond Acceptors (HBA)
* TPSA (Topological Polar Surface Area)
* Number of atoms

---

###  Handling Imbalance

* Dataset was highly imbalanced
* Applied **SMOTE (Synthetic Minority Oversampling Technique)**

 Improved model’s ability to detect toxic compounds

---

###  Model Training

* Algorithm: **Random Forest Classifier**
* Train/Test Split: 80/20

---

###  Model Optimization

* Initial issue: low recall (~0.38)
* Applied:

  * SMOTE
  * **Threshold tuning (optimal ≈ 0.27)**

---

###  Final Performance

* Accuracy: ~0.64
* Recall: ~0.75 (priority metric)
* F1 Score: improved

Focused on **minimizing false negatives** (critical for toxicity)

---

## 🌐 Web Application

### 🖥️ Frontend

* Built using:

  * HTML
  * Tailwind CSS
  * JavaScript

Features:

* SMILES input
* Predict button
* Color-coded toxicity result
* Descriptor insights
* Explanation & alternative suggestion

---

### ⚙️ Backend

* Built using Python + Flask

Workflow:

```
SMILES → RDKit → Feature Extraction → ML Model → Prediction → UI Output
```

---

##  Tech Stack

* Python
* Flask
* RDKit
* Scikit-learn
* Tailwind CSS
* JavaScript
* Google Colab
  
---

## 📁 Project Structure

```
Safe-Synthesis/
│
├── model/
│   ├── random_forest_model.joblib
│   ├── train_model.py
│
├── static/
│   └── structure.png
│
├── templates/
│   └── index.html
│
├── app.py
├── README.md
```

---

## How to Run

### 1. Clone the repository

```
git clone https://github.com/your-username/Safe-Synthesis.git
cd Safe-Synthesis
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Run the application

```
python app.py
```

---

### 4. Open in browser

```
http://127.0.0.1:5000
```

---

## ⚠️ Limitations

* Model trained on **single endpoint (SR-ARE)**
* Uses **basic molecular descriptors only**
* Alternative suggestion is **mock-based**
* No real-time research integration

---

## Future Scope

* Multi-target toxicity prediction
* Deep learning on molecular structures
* Integration with research databases (e.g., PubChem)
* Explainable AI (feature importance, SHAP)
* Real chemical similarity search
* User authentication & history

---

## Conclusion

Safe Synthesis demonstrates how AI can be used to:

* Predict chemical toxicity
* Improve research safety
* Reduce trial-and-error

Moving toward **safer, smarter chemical design**

---

## Acknowledgement

This project was developed with guidance, self-learning, and AI-assisted tools to accelerate development while focusing on understanding and system design.

---

##  Author

**Aditi Goyal**

---

 If you found this project useful, consider giving it a star!
