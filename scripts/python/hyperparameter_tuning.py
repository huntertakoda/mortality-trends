import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.impute import SimpleImputer
from scipy.stats import randint, uniform

# file paths

input_file = "C:/data/selected_features_mortality_data.csv"

# load the dataset

print("loading dataset...")
data = pd.read_csv(input_file)

# define features (X) and target variable (y)

X = data.drop(columns=["infant_death_flag"])
y = data["infant_death_flag"]

# handle missing values

print("handling missing values...")
imputer = SimpleImputer(strategy="mean")
X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

# split into train and test sets

print("splitting dataset into train and test...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# define parameter distributions for RandomizedSearchCV

rf_param_dist = {
    "n_estimators": randint(50, 300),
    "max_depth": [None] + list(range(5, 30)),
    "min_samples_split": randint(2, 10),
    "min_samples_leaf": randint(1, 5),
}
gb_param_dist = {
    "n_estimators": randint(50, 300),
    "learning_rate": uniform(0.01, 0.2),
    "max_depth": list(range(3, 10)),
}

# train and tune Random Forest with RandomizedSearchCV

print("tuning random forest model...")
rf_random = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    rf_param_dist,
    n_iter=20,
    scoring="roc_auc",
    cv=3,
    random_state=42,
    n_jobs=-1,
)
rf_random.fit(X_train, y_train)
best_rf_model = rf_random.best_estimator_
print("best parameters for random forest:", rf_random.best_params_)

# train and tune Gradient Boosting with RandomizedSearchCV

print("tuning gradient boosting model...")
gb_random = RandomizedSearchCV(
    GradientBoostingClassifier(random_state=42),
    gb_param_dist,
    n_iter=20,
    scoring="roc_auc",
    cv=3,
    random_state=42,
    n_jobs=-1,
)
gb_random.fit(X_train, y_train)
best_gb_model = gb_random.best_estimator_
print("best parameters for gradient boosting:", gb_random.best_params_)

# save tuned models

import joblib

print("saving tuned models...")
joblib.dump(best_rf_model, "C:/data/best_rf_model.pkl")
joblib.dump(best_gb_model, "C:/data/best_gb_model.pkl")
print("models saved successfully!")
