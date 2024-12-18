import pandas as pd
import numpy as np

# file paths

input_file = "C:/data/transformed_mortality_data.csv"
output_file = "C:/data/feature_enhanced_mortality_data.csv"

# load the dataset

print("loading dataset...")
data = pd.read_csv(input_file)

# inspect dataset

print("dataset shape:", data.shape)
print("columns:", list(data.columns))

# create new features

print("creating new features...")

# interaction term: socioeconomic index multiplied by co-morbidity count

data["socio_co_morbidity_interaction"] = data["socioeconomic_index"] * data["co_morbidity_count"]

# log transformation of socioeconomic index (adding 1 to avoid log(0))

data["log_socioeconomic_index"] = np.log1p(data["socioeconomic_index"])

# binary feature: high-risk flag (e.g., age >= 65 or co-morbidity count >= 3)

data["high_risk_flag"] = np.where((data["age"] >= 65) | (data["co_morbidity_count"] >= 3), 1, 0)

# normalize a feature: cause_of_death encoded to frequencies (if categorical)

if "cause_of_death" in data.columns:
    cause_counts = data["cause_of_death"].value_counts(normalize=True)
    data["cause_of_death_frequency"] = data["cause_of_death"].map(cause_counts)

# inspect new features

print("new features created:")
print(data.head())

# save enhanced dataset

data.to_csv(output_file, index=False)
print(f"feature-enhanced dataset saved to {output_file}")
