# Fraud Detection in Financial Transactions

A machine learning project to **predict fraudulent financial transactions** using behavioral, transactional, and device signals. The workflow covers EDA, preprocessing, feature engineering, model comparison, and threshold tuning for better fraud capture (high recall).

> **Course/Group Project** — includes collaborative work and shared deliverables.

---

## Project goal

Build and compare supervised ML models to classify transactions as:
- **0** = Not Fraud  
- **1** = Fraud

The dataset is **highly imbalanced** (fraud is rare), so the primary focus is on **Recall**, **F1-score**, and **ROC–AUC**, not just overall accuracy. 

---

## What’s inside

- **Notebook (end-to-end pipeline):** `notebooks/Fraud_Detection_Group6.ipynb`
- **Dataset:** `data/raw/fraud_detection_dataset.csv`
- **Presentation deck:** `docs/Final_Fraud_Detection_Presentation.pptx`

---

## Dataset overview

- **Total features:** 12  
- **Target:** `Fraudulent` (0/1) 
- Missing values appear mostly in **categorical fields** = 
- Key behavioral signals highlighted during EDA:
  - `Hours_Since_Last_Transaction`
  - `Number_of_Transactions_Last_24H`
  - `Device_Used` 

---

## Work done

### 1) Exploratory Data Analysis (EDA)
We explored fraud behavior across:
- **Transaction velocity** (e.g., spikes around ~6 transactions in last 24 hours) 
- **Time-of-day patterns** (fraud blends into normal traffic)  
- **Location patterns** (some cities show higher fraud rates)  
- **Correlation** (low multicollinearity; features provide mostly independent signal)   

### 2) Data cleaning & preprocessing
- Checked missing values and datatypes
- Standardized categorical formats  
- One-hot encoded categorical variables (transaction type, device, payment method)  
- Engineered: **`Hours_Since_Last_Transaction`**
- Used **train/test split**
- Addressed class imbalance mainly with **probability threshold tuning** instead of oversampling 

### 3) Modeling
Trained and evaluated:
- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost  

We tuned the decision threshold (0.50 → **0.20**) to improve fraud capture (recall). 

---

## Results (from the notebook run)

Using the tuned threshold (0.20), the best-performing model was XGBoost with:

Recall: 0.8759

F1-score: 0.3279

ROC–AUC: 0.8279

Accuracy: 0.5318

XGBoost provided the best balance between fraud detection capability (high recall) and overall discrimination (ROC–AUC), making it the most suitable model for this imbalanced fraud detection problem.

---

## Explainability: top drivers

Feature importance analysis (XGBoost) emphasized:
- Risky **transaction types** (e.g., bank transfer / POS / online purchase)
- **Device signals** (tablet/mobile/unknown)
- **Behavioral timing** (hours since last transaction; transaction velocity) 

---

## Challenges

- **Severe class imbalance:** accuracy can look “okay” while missing fraud → prioritized recall + threshold tuning.
- **Missing categorical data:** required careful cleaning and encoding. 
- **False positives vs false negatives tradeoff:** improved fraud capture by lowering the probability threshold to 0.20. 

---

## Business impact

A model like this can help:
- **Reduce financial losses** by catching more fraud earlier
- Improve real-time monitoring using **behavior + device + transaction-type** signals
- Support fraud operations teams with actionable risk factors 

---

## Future considerations

- Calibrate probabilities and set **cost-based thresholds** (fraud loss vs review cost)
- Add richer behavioral features (rolling windows, merchant-level patterns)
- Add explainability tooling (e.g., SHAP) for case-level reasoning
- Evaluate fairness/risk across regions/devices and monitor drift
- Package into an API + streaming scoring pipeline for real-time detection

---

## Repo structure

```text
fraud-detection-financial-transactions/
├─ data/
│  ├─ raw/                         # original dataset
│  ├─ processed/                   # place processed exports here
│  └─ README.md
├─ notebooks/
│  └─ Fraud_Detection_Group6.ipynb # full workflow (recommended)
├─ docs/
│  └─ Final_Fraud_Detection_Presentation.pptx
├─ src/                            # starter scripts for productionization
├─ results/
│  ├─ figures/
│  └─ metrics/
├─ requirements.txt
├─ environment.yml
└─ README.md
```

---

## How to run

### Option A: pip
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

Open: `notebooks/Fraud_Detection_Group6.ipynb`

### Option B: conda
```bash
conda env create -f environment.yml
conda activate fraud-detection
jupyter notebook
```

---

## Credits

Group members listed in the presentation. 
