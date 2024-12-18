import pandas as pd
from sklearn.model_selection import train_test_split

# file paths

input_file = "C:/data/transformed_mortality_data.csv"
train_output = "C:/data/train_data.csv"
test_output = "C:/data/test_data.csv"

# load the transformed dataset

print("loading dataset...")
data = pd.read_csv(input_file)

# inspect the dataset

print("dataset shape:", data.shape)
print("columns:", list(data.columns))

# define features (X) and target variable (y)

features = ["age", "co_morbidity_count", "socioeconomic_index", "age_squared", "co_morbidity_per_age"]
target = "infant_death_flag" 

print("features:", features)
print("target:", target)

# separate features and target

X = data[features]
y = data[target]

# split the dataset into training and testing sets

print("splitting dataset into train and test...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# combine features and target back for saving

train_data = pd.concat([X_train, y_train], axis=1)
test_data = pd.concat([X_test, y_test], axis=1)

# save the train and test datasets

train_data.to_csv(train_output, index=False)
test_data.to_csv(test_output, index=False)

print(f"training dataset saved to: {train_output}")
print(f"testing dataset saved to: {test_output}")
print("train-test split completed.")
