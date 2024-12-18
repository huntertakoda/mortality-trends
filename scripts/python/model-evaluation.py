import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import seaborn as sns

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

# train Random Forest and Gradient Boosting models (using default parameters for simplicity)

print("training models...")
rf_model = RandomForestClassifier(random_state=42, n_estimators=100).fit(X_train, y_train)
gb_model = GradientBoostingClassifier(random_state=42, n_estimators=100).fit(X_train, y_train)

# make predictions

print("making predictions...")
rf_pred = rf_model.predict(X_test)
gb_pred = gb_model.predict(X_test)

# function for evaluation metrics

def evaluate_model(name, y_test, y_pred):
    print(f"evaluating {name}...")
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1": f1_score(y_test, y_pred),
    }
    for metric, value in metrics.items():
        print(f"{name} {metric}: {value:.4f}")
    print(f"{name} classification report:\n", classification_report(y_test, y_pred))
    cm = confusion_matrix(y_test, y_pred)
    return cm

# evaluate Random Forest

rf_cm = evaluate_model("random forest", y_test, rf_pred)

# evaluate Gradient Boosting

gb_cm = evaluate_model("gradient boosting", y_test, gb_pred)

# plot confusion matrices

def plot_confusion_matrix(cm, title):
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["No", "Yes"], yticklabels=["No", "Yes"])
    plt.title(title)
    plt.ylabel("Actual")
    plt.xlabel("Predicted")
    plt.show()

plot_confusion_matrix(rf_cm, "Random Forest Confusion Matrix")
plot_confusion_matrix(gb_cm, "Gradient Boosting Confusion Matrix")
