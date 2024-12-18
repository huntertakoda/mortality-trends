from scipy.stats import chi2_contingency, ttest_ind
import pandas as pd
import numpy as np

# file paths

dataset_path = "C:/data/selected_features_mortality_data.csv"

# load dataset

print("loading dataset...")
data = pd.read_csv(dataset_path)

# recreate age_group column if missing

if "age_group" not in data.columns:
    print("recreating age_group column...")
    bins = [0, 1, 18, 64, 120]  
    labels = ["Infant", "Child", "Adult", "Elderly"]
    data["age_group"] = pd.cut(data["age"], bins=bins, labels=labels, right=False)

# check for socioeconomic_index column

if "socioeconomic_index" not in data.columns:
    print("socioeconomic_index column missing! Recalculating...")
    if "log_socioeconomic_index" in data.columns:
        data["socioeconomic_index"] = data["log_socioeconomic_index"].apply(lambda x: 10 ** x)
    else:
        raise KeyError("socioeconomic_index column is missing and cannot be recalculated!")

# chi-squared test: age group vs infant death flag

print("performing chi-squared test...")
contingency_table = pd.crosstab(data["age_group"], data["infant_death_flag"])
chi2, p, dof, expected = chi2_contingency(contingency_table)
print(f"chi2: {chi2:.4f}, p-value: {p:.4f}")

# t-test: comparing socioeconomic index for infant death cases

print("performing t-test...")
soc_index_true = data.loc[data["infant_death_flag"] == 1, "socioeconomic_index"].dropna()
soc_index_false = data.loc[data["infant_death_flag"] == 0, "socioeconomic_index"].dropna()

# Check if groups have sufficient data

if len(soc_index_true) < 2 or len(soc_index_false) < 2:
    print("Insufficient data for t-test. Check groups for non-NaN values.")
else:
    t_stat, p_val = ttest_ind(soc_index_true, soc_index_false, equal_var=False)
    print(f"t-statistic: {t_stat:.4f}, p-value: {p_val:.4f}")
