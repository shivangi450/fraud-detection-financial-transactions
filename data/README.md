# Data

This project uses a tabular dataset of financial transactions with a binary target label:

- `Fraudulent` (0 = Not Fraud, 1 = Fraud)

The raw dataset is stored in `data/raw/fraud_detection_dataset.csv`.

## Notes
- The dataset is **highly imbalanced** (fraud is rare), so evaluation focuses on **Recall**, **F1**, and **ROC–AUC**.
- Categorical fields contain missing values in the raw data and are handled during preprocessing in the notebook.
