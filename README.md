# Corporate Burnout Risk Mitigation: Predictive Modeling & System Explainability

<p align="center">
  <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExejVoZDdxZHcwOXo3eXQwdXZnbjdkZnh2MmVjZGYzaWx2b2Jla3p0eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/lJEGgG5ajs4zC/giphy.gif" width="350" alt="System Workflow Analytics Data Pipeline">
</p>

##  Executive Summary
Employee burnout represents a massive operational bottleneck in the technology sector, resulting in unexpected pipeline delays, reduced software performance, and high talent replacement costs. 

This project builds an end-to-end predictive decision system leveraging the Open Sourcing Mental Illness (OSMI) Mental Health in Tech Survey dataset. By combining XGBoost gradient-boosting frameworks with SHAP (SHapley Additive exPlanations), the system shifts HR strategy from reactive accommodation to proactive risk intervention, allowing enterprises to diagnose systemic workplace stressors before they impact retention.

---

##  Tech Stack & Systems Architecture
- **Data Curation & Processing:** Pandas, NumPy, Scikit-Learn
- **Feature Engineering:** Quantitative mapping of psychological safety parameters and workplace structure factors
- **Predictive Engine:** XGBoost Classifier
- **Model Explainability Engine:** SHAP Framework
- **Data Visualization:** Seaborn, Matplotlib

---

##  Core Discovery & Machine Learning Results
- **Balanced Targeting:** Initial EDA revealed a highly balanced target distribution (~50.6% vs 49.4% treatment seeking rates), removing the requirement for synthetic oversampling (SMOTE).
- **Enterprise-Scale Stressors:** Workplace size analysis reveals distinct spikes in behavioral risk indicators inside larger technology infrastructures (1000+ employees), indicating exactly where preventative infrastructure is required most.

---

##  Repository Blueprint
- `src/data_preprocessing.py`: Handles missing value strategies, state/country filter pipelines, and categorical encoding.
- `src/model_pipeline.py`: Runs the train-test splits, optimizes the XGBoost classifier, and extracts global/local SHAP values.
- `notebooks/`: Contains exploratory data analysis and initial visualization playbooks.

---

##  How to Run the Infrastructure

1. Clone this repository:
```bash
   git clone [https://github.com/YOUR_USERNAME/mental-health-burnout-ml.git](https://github.com/YOUR_USERNAME/mental-health-burnout-ml.git)
   cd mental-health-burnout-ml
Install dependencies:

Bash
   pip install -r requirements.txt
Data Source Setup:
Download the source data directly from the Kaggle OSMI Mental Health in Tech Survey. Place the survey.csv file inside the data/ directory before executing the pipeline.
```

