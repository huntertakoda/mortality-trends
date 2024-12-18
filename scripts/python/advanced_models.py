import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
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

# train Random Forest model

print("training random forest model...")
rf_model = RandomForestClassifier(random_state=42, n_estimators=100)
rf_model.fit(X_train, y_train)

# train Gradient Boosting model

print("training gradient boosting model...")
gb_model = GradientBoostingClassifier(random_state=42, n_estimators=100)
gb_model.fit(X_train, y_train)

# make predictions for both models

print("making predictions...")
rf_pred = rf_model.predict(X_test)
rf_pred_proba = rf_model.predict_proba(X_test)[:, 1]

gb_pred = gb_model.predict(X_test)
gb_pred_proba = gb_model.predict_proba(X_test)[:, 1]

# evaluate models

print("evaluating random forest model...")
rf_metrics = {
    "accuracy": accuracy_score(y_test, rf_pred),
    "precision": precision_score(y_test, rf_pred),
    "recall": recall_score(y_test, rf_pred),
    "f1": f1_score(y_test, rf_pred),
    "roc_auc": roc_auc_score(y_test, rf_pred_proba),
}
for metric, value in rf_metrics.items():
    print(f"random forest {metric}: {value:.4f}")

print("evaluating gradient boosting model...")
gb_metrics = {
    "accuracy": accuracy_score(y_test, gb_pred),
    "precision": precision_score(y_test, gb_pred),
    "recall": recall_score(y_test, gb_pred),
    "f1": f1_score(y_test, gb_pred),
    "roc_auc": roc_auc_score(y_test, gb_pred_proba),
}
for metric, value in gb_metrics.items():
    print(f"gradient boosting {metric}: {value:.4f}")

