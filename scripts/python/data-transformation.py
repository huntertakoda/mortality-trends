import pandas as pd
import os
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# file paths

input_file = "C:/data/clean_mortality_data.csv"
output_file = "C:/data/transformed_mortality_data.csv"

# load dataset

print("loading dataset...")
data = pd.read_csv(input_file)

# inspect data

print("dataset shape:", data.shape)
print("columns:", list(data.columns))

# select numerical columns for scaling

numerical_columns = ["age", "co_morbidity_count", "socioeconomic_index"]
print("numerical columns to be transformed:", numerical_columns)

# apply standard scaling (z-score)
scaler = StandardScaler()
data_scaled = data.copy()
data_scaled[numerical_columns] = scaler.fit_transform(data[numerical_columns])

# create new features

print("adding new features...")
data_scaled["age_squared"] = data_scaled["age"] ** 2
data_scaled["co_morbidity_per_age"] = (
    data_scaled["co_morbidity_count"] / data_scaled["age"]
).replace([float("inf"), -float("inf")], 0)

# check transformation results

print("transformation completed.")
print(data_scaled.head())

# save the transformed dataset

data_scaled.to_csv(output_file, index=False)
print(f"transformed dataset saved to {output_file}")
