import joblib
import pandas as pd
import json

# file paths

rf_model_path = "C:/data/best_rf_model.pkl"
gb_model_path = "C:/data/best_gb_model.pkl"
report_path = "C:/data/model_summary_report.json"

# load models

print("loading tuned models...")
rf_model = joblib.load(rf_model_path)
gb_model = joblib.load(gb_model_path)

# extract feature importances

print("extracting feature importances...")
rf_feature_importances = rf_model.feature_importances_
gb_feature_importances = gb_model.feature_importances_

# prepare summary report

print("preparing summary report...")
model_summary = {
    "Random Forest": {
        "Best Parameters": rf_model.get_params(),
        "Feature Importances": list(rf_feature_importances),
    },
    "Gradient Boosting": {
        "Best Parameters": gb_model.get_params(),
        "Feature Importances": list(gb_feature_importances),
    },
}

# save summary report

print("saving summary report...")
with open(report_path, "w") as f:
    json.dump(model_summary, f, indent=4)
print(f"summary report saved to {report_path}")

# save models for reuse

print("re-saving models...")
joblib.dump(rf_model, rf_model_path)
joblib.dump(gb_model, gb_model_path)
print("models saved successfully!")

# load summary report for verification

with open(report_path, "r") as f:
    summary_loaded = json.load(f)
print("summary report loaded for verification:")
print(json.dumps(summary_loaded, indent=4))
