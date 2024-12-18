import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error

# file paths

rf_model_path = "C:/data/best_rf_model.pkl"
gb_model_path = "C:/data/best_gb_model.pkl"
dataset_path = "C:/data/selected_features_mortality_data.csv"

# load dataset

print("loading dataset...")
data = pd.read_csv(dataset_path)
X = data.drop(columns=["infant_death_flag"])
y = data["infant_death_flag"]

# handle missing values

print("handling missing values...")
imputer = SimpleImputer(strategy="mean")
X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

# load tuned models

print("loading tuned models...")
rf_model = joblib.load(rf_model_path)
gb_model = joblib.load(gb_model_path)

# make predictions

print("making predictions...")
rf_pred_proba = rf_model.predict_proba(X)[:, 1]
gb_pred_proba = gb_model.predict_proba(X)[:, 1]

# calculate residuals (actual - predicted probabilities)

print("calculating residuals...")
rf_residuals = y - rf_pred_proba
gb_residuals = y - gb_pred_proba

# calculate mean squared error

rf_mse = mean_squared_error(y, rf_pred_proba)
gb_mse = mean_squared_error(y, gb_pred_proba)
print(f"random forest mse: {rf_mse:.4f}")
print(f"gradient boosting mse: {gb_mse:.4f}")

# plot residuals

def plot_residuals(residuals, model_name):
    plt.figure(figsize=(10, 6))
    sns.histplot(residuals, bins=30, kde=True)
    plt.title(f"{model_name} Residuals Distribution")
    plt.xlabel("Residuals")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

print("plotting residuals...")
plot_residuals(rf_residuals, "Random Forest")
plot_residuals(gb_residuals, "Gradient Boosting")

# plot actual vs predicted probabilities

def plot_actual_vs_predicted(y_true, y_pred_proba, model_name):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=y_pred_proba, y=y_true, alpha=0.5)
    plt.title(f"{model_name} Actual vs Predicted Probabilities")
    plt.xlabel("Predicted Probabilities")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.show()

print("plotting actual vs predicted probabilities...")
plot_actual_vs_predicted(y, rf_pred_proba, "Random Forest")
plot_actual_vs_predicted(y, gb_pred_proba, "Gradient Boosting")
