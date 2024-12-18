import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# file paths

input_file = "C:/data/selected_features_mortality_data.csv"

# load the dataset

print("loading dataset...")
data = pd.read_csv(input_file)

# inspect the dataset

print("dataset shape:", data.shape)
print("columns:", list(data.columns))

# define features (X) and target variable (y)

X = data.drop(columns=["infant_death_flag"])
y = data["infant_death_flag"]

# handle missing values by imputing with mean

print("handling missing values...")
imputer = SimpleImputer(strategy="mean")
X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

# split into train and test sets

print("splitting dataset into train and test...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# train logistic regression model

print("training logistic regression model...")
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train, y_train)

# make predictions

print("making predictions...")
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]

# evaluate the model

print("evaluating model...")
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)

# print evaluation metrics

print("baseline model evaluation:")
print(f"accuracy: {accuracy:.4f}")
print(f"precision: {precision:.4f}")
print(f"recall: {recall:.4f}")
print(f"f1-score: {f1:.4f}")
print(f"roc-auc: {roc_auc:.4f}")
