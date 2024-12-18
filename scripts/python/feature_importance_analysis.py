import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# file paths

rf_model_path = "C:/data/best_rf_model.pkl"
gb_model_path = "C:/data/best_gb_model.pkl"
dataset_path = "C:/data/selected_features_mortality_data.csv"

# load dataset for feature names

print("loading dataset...")
data = pd.read_csv(dataset_path)
feature_names = data.drop(columns=["infant_death_flag"]).columns.tolist()

# load tuned models

print("loading tuned models...")
rf_model = joblib.load(rf_model_path)
gb_model = joblib.load(gb_model_path)

# extract feature importances

print("extracting feature importances...")
rf_importances = rf_model.feature_importances_
gb_importances = gb_model.feature_importances_

# create dataframes for visualization

rf_df = pd.DataFrame({"Feature": feature_names, "Importance": rf_importances}).sort_values(by="Importance", ascending=False)
gb_df = pd.DataFrame({"Feature": feature_names, "Importance": gb_importances}).sort_values(by="Importance", ascending=False)

# visualize feature importances

def plot_feature_importance(df, model_name):
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Importance", y="Feature", data=df)
    plt.title(f"{model_name} Feature Importance")
    plt.xlabel("Importance")
    plt.ylabel("Feature")
    plt.tight_layout()
    plt.show()

print("plotting feature importances...")
plot_feature_importance(rf_df, "Random Forest")
plot_feature_importance(gb_df, "Gradient Boosting")
