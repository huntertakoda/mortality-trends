import pandas as pd
import os

# file paths

input_file = "C:/data/cleaned_mortality_data.csv"
output_file = "C:/data/clean_mortality_data.csv"

# load dataset

print("loading dataset...")
data = pd.read_csv(input_file)

# inspect columns

print("columns in dataset:", data.columns)

# clean column names: lowercased, spaces and hyphens replaced with underscores

data.columns = data.columns.str.lower().str.replace(" ", "_").str.replace("-", "_")
print("cleaned column names:", data.columns)

# drop duplicates

print("removing duplicate rows...")
data = data.drop_duplicates()

# drop invalid rows: negative values

print("removing invalid rows...")
data = data[
    (data["age"] >= 0) &
    (data["co_morbidity_count"] >= 0) &
    (data["socioeconomic_index"] >= 0)
]

# check missing values

print("checking for missing values...")
missing_values = data.isnull().sum()
print("missing values per column:\n", missing_values)

# drop rows with missing data

print("removing rows with missing values...")
data = data.dropna()

# log the cleaning process

print("final dataset shape:", data.shape)
with open("C:/data/cleaning_log.txt", "w") as log:
    log.write(f"columns found: {list(data.columns)}\n")
    log.write(f"missing values:\n{missing_values}\n")
    log.write("cleaning completed successfully.\n")

# save cleaned dataset

data.to_csv(output_file, index=False)
print(f"cleaned dataset saved to {output_file}")

