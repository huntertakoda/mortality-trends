import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.impute import SimpleImputer

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

# define parameter grids for GridSearchCV

rf_param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [None, 10, 20],
    "min_samples_split": [2, 5],
    "min_samples_leaf": [1, 2],
}
gb_param_grid = {
    "n_estimators": [100, 200],
    "learning_rate": [0.1, 0.01],
    "max_depth": [3, 5],
}

# train and tune Random Forest model

print("tuning random forest model...")
rf_grid = GridSearchCV(RandomForestClassifier(random_state=42), rf_param_grid, cv=3, scoring="roc_auc", n_jobs=-1)
rf_grid.fit(X_train, y_train)
best_rf_model = rf_grid.best_estimator_
print("best parameters for random forest:", rf_grid.best_params_)

# train and tune Gradient Boosting model

print("tuning gradient boosting model...")
gb_grid = GridSearchCV(GradientBoostingClassifier(random_state=42), gb_param_grid, cv=3, scoring="roc_auc", n_jobs=-1)
gb_grid.fit(X_train, y_train)
best_gb_model = gb_grid.best_estimator_
print("best parameters for gradient boosting:", gb_grid.best_params_)

# make predictions with tuned models

print("making predictions with tuned models...")
rf_pred = best_rf_model.predict(X_test)
rf_pred_proba = best_rf_model.predict_proba(X_test)[:, 1]

gb_pred = best_gb_model.predict(X_test)
gb_pred_proba = best_gb_model.predict_proba(X_test)[:, 1]

# evaluate tuned models

def evaluate_model(name, y_test, y_pred, y_pred_proba):
    print(f"evaluating {name}...")
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1": f1_score(y_test, y_pred),
        "roc_auc": roc_auc_score(y_test, y_pred_proba),
    }
    for metric, value in metrics.items():
        print(f"{name} {metric}: {value:.4f}")
    return metrics

rf_metrics = evaluate_model("random forest", y_test, rf_pred, rf_pred_proba)
gb_metrics = evaluate_model("gradient boosting", y_test, gb_pred, gb_pred_proba)
