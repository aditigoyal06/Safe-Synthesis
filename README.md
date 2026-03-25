# ***Safe Synthesis: AI-Driven Drug Toxicity Prediction***
--- 
### **Project Overview**
Safe Synthesis is an advanced machine learning solution developed for the Codecure - AI Hackathon (Track A). 
Drug development frequently fails due to unexpected toxicity, which increases costs and risks patient safety. 
This project builds a predictive model to identify toxic compounds early in the pipeline using molecular descriptors.

---
## **The Problem**
**High Failure Rates**: Many drug candidates fail during clinical trials due to late-stage toxicity discovery.
**Cost Efficiency**: Early prediction significantly reduces development overhead and resource waste.
**Safety First**: Improving the screening process ensures only the safest compounds proceed to human testing.

---
## **Dataset & FeaturesPrimary Dataset:** 
**Tox21 Dataset** containing ~12,000 chemical compounds with toxicity assay results and molecular structures.
**Secondary Data**: ZINC-250k for exploring chemical space and engineering additional features like logP, QED, and SAS.
**Input Format**: Molecular structures represented as SMILES strings.

---
## **Tech Stack & ToolsLanguage:** 
**Python** (Core logic and Model training)
**Web Framework**: Flask (For the prediction interface)
**Data Science**: Pandas, Scikit-learn (Preprocessing and ML)
**Frontend**: HTML, CSS (User Dashboard)

---
## **Technical WorkflowData Preprocessing:** 
**EDA**: Cleaning the Tox21 dataset and handling molecular descriptor data.
**Feature Engineering**: Converting SMILES strings into numerical data for the model.
**Model Training**: Implementing classification models to predict toxicity risk.
**Interpretability**: Analyzing which molecular properties (structural features) contribute most to toxicity.
**Interface**: A simple web tool to evaluate new compounds.

---
## **Future ScopeReal-time Visualization:**
**Integrating interactive charts** to show relationships between molecular properties and toxicity.
**Broader Databases:** Incorporating the ChEMBL Bioactivity Dataset for enhanced pharmacological insights.
**Generative AI Integration**: Using AI to suggest structural modifications that reduce the toxicity of a candidate drug.

---
