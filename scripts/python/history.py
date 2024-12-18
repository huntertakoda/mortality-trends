# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Fri Nov 29 21:57:05 2024)---
%runfile C:/Users/yanfr/.spyder-py3/temp.py --wdir

## ---(Fri Nov 29 23:17:52 2024)---
%runfile C:/Users/yanfr/.spyder-py3/temp.py --wdir

## ---(Sun Dec  1 18:26:57 2024)---
%runfile C:/Users/yanfr/.spyder-py3/temp.py --wdir
%runfile c:/users/yanfr/.spyder-py3/untitled0.py --wdir
%runfile c:/users/yanfr/.spyder-py3/untitled1.py --wdir
pip install imbalanced-learn
pip install imbalanced-learn
%runfile c:/users/yanfr/.spyder-py3/untitled1.py --wdir

## ---(Sun Dec  1 21:15:39 2024)---
%runfile C:/Users/yanfr/.spyder-py3/healthcarefd_models.py --wdir
pip install imbalanced-learn
imbalanced-learn
pip install imbalanced-learn
%runfile C:/Users/yanfr/.spyder-py3/healthcarefd_models.py --wdir
%runfile C:/Users/yanfr/.spyder-py3/updatedparameters.py --wdir
%runfile C:/Users/yanfr/.spyder-py3/hyperparameters.py --wdir
%runfile C:/Users/yanfr/.spyder-py3/hyperparameters2.py --wdir
%runfile C:/Users/yanfr/.spyder-py3/untitled3.py --wdir

## ---(Tue Dec  3 13:38:47 2024)---
%runfile C:/Users/yanfr/.spyder-py3/untitled0.py --wdir

## ---(Wed Dec  4 19:20:08 2024)---
%runfile C:/Users/yanfr/untitled0.py --wdir

## ---(Wed Dec  4 19:25:44 2024)---
%runfile C:/Users/yanfr/untitled0.py --wdir
%runfile C:/Users/yanfr/untitled0.py --wdir
%runfile C:/Users/yanfr/untitled1.py --wdir
%runfile C:/Users/yanfr/untitled0.py --wdir
%runfile C:/Users/yanfr/untitled1.py --wdir
%runfile C:/Users/yanfr/algorithmictrading/visualization.py --wdir
%runfile C:/Users/yanfr/algorithmictrading/feature_engineering.py --wdir
%runfile C:/Users/yanfr/algorithmictrading/developing_model.py --wdir
%runfile C:/Users/yanfr/algorithmictrading/model_analysis.py --wdir
import pandas as pd

# Load the enhanced data
btc_data = pd.read_csv('BTC_Featured.csv')

# Define the target column: 1 if next day's price > current price, 0 otherwise
btc_data['target'] = (btc_data['BTC_price'].shift(-1) > btc_data['BTC_price']).astype(int)

# Drop the last row since it has no target value
btc_data = btc_data[:-1]

# Save the updated dataset
btc_data.to_csv('BTC_Featured.csv', index=False)

print("Target column added and dataset updated!")


%runfile C:/Users/yanfr/algorithmictrading/model_analysis.py --wdir
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

# Define features and target
features = ['BTC_price', 'daily_return', 'MA7', 'MA30', 'volatility']
X = btc_data[features]
y = btc_data['target']

# Train/Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Instantiate and train the Random Forest Classifier
model = RandomForestClassifier(random_state=42, n_estimators=100)
model.fit(X_train, y_train)

print("Model trained successfully!")

%runfile C:/Users/yanfr/algorithmictrading/model_analysis.py --wdir
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# loading

btc_data = pd.read_csv('BTC_Featured.csv')

features = ['BTC_price', 'daily_return', 'MA7', 'MA30', 'volatility']
X = btc_data[features]
y = btc_data['target']

model.fit(X, y)  #
importance = model.feature_importances_

# visualization dataframe

feature_importance_df = pd.DataFrame({'Feature': features, 'Importance': importance})
feature_importance_df.sort_values(by='Importance', ascending=False, inplace=True)

# ftre hierarchy

plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feature_importance_df, palette='viridis')
plt.title('Feature Importance', fontsize=16)
plt.xlabel('Importance', fontsize=12)
plt.ylabel('Feature', fontsize=12)
plt.show()


%runfile C:/Users/yanfr/algorithmictrading/model_analysis.py --wdir
%runfile C:/Users/yanfr/algorithmictrading/feature_addition.py --wdir
%runfile C:/Users/yanfr/algorithmictrading/retraining.py --wdir
%runfile C:/Users/yanfr/algorithmictrading/retargeting.py --wdir
%runfile C:/Users/yanfr/algorithmictrading/retraining.py --wdir
%runfile C:/Users/yanfr/algorithmictrading/untitled9.py --wdir

## ---(Thu Dec  5 21:18:22 2024)---
%runfile C:/Users/yanfr/untitled0.py --wdir
%runfile C:/Users/yanfr/untitled0.py --wdir
%runfile C:/Users/yanfr/untitled1.py --wdir
%runfile C:/Users/yanfr/algorithmictrading/xgboost_evaluation.py --wdir
%runfile C:/Users/yanfr/algorithmictrading/xgboost_backtest.py --wdir
%runfile C:/Users/yanfr/algorithmictrading/xgboost_threshold_optimization.py --wdir
%runfile C:/Users/yanfr/algorithmictrading/untitled5.py --wdir
%runfile C:/Users/yanfr/algorithmictrading/xgboost_backtest_optimal_threshold.py --wdir
%runfile C:/Users/yanfr/algorithmictrading/xgboost_backtest_with_transaction_costs.py..py --wdir
%runfile C:/Users/yanfr/algorithmictrading/periodic_testing.py --wdir
%runfile C:/Users/yanfr/algorithmictrading/untitled9.py --wdir
%runfile C:/Users/yanfr/algorithmictrading/untitled10.py --wdir
%runfile C:/Users/yanfr/algorithmictrading/untitled11.py --wdir
%runfile C:/Users/yanfr/algorithmictrading/xgboost_backtest_with_transaction_costs.py..py --wdir

## ---(Fri Dec  6 00:39:53 2024)---
%runfile C:/Users/yanfr/untitled2.py --wdir
%runfile C:/Users/yanfr/untitled2.py --wdir
%runfile C:/information_generator/main.py --wdir
uvicorn main:app --reload
uvicorn main:app --reload]
%runfile c:/information_generator/untitled3.py --wdir
>>> from app import db
>>> db.create_all()

## ---(Fri Dec  6 17:41:36 2024)---
%runfile C:/personalizedlearningpathway/app.py --wdir
from app import db
db.create_all()
from app import app, db

# setting up the application context
with app.app_context():
    db.create_all()
    
%runfile C:/personalizedlearningpathway/app.py --wdir
from app import db
with app.app_context():
    db.create_all()
    
%runfile C:/personalizedlearningpathway/app.py --wdir
from app import db, app  # import db and app from app.py

# set the app context
with app.app_context():
    db.create_all()
    
%runfile C:/personalizedlearningpathway/app.py --wdir

## ---(Fri Dec  6 22:30:37 2024)---
%runfile C:/nlpsentimentanalysis/mental_health_analysis.py --wdir
%runfile C:/nlpsentimentanalysis/mental_health_analysis.py --wdir
%runfile C:/nlpsentimentanalysis/untitled4.py --wdir
%runfile C:/nlpsentimentanalysis/untitled5.py --wdir
%runfile C:/nlpsentimentanalysis/untitled6.py --wdir
%runfile C:/nlpsentimentanalysis/untitled6.py --wdir
%runfile C:/nlpsentimentanalysis/untitled6.py --wdir

## ---(Tue Dec 10 01:12:00 2024)---
%runfile C:/nlpsentimentanalysis/untitled3.py --wdir
%runfile C:/Windows/System32/purple_env/Lib/site-packages/transformers/utils/import_utils.py --wdir
%runfile C:/Windows/System32/purple_env/Lib/site-packages/transformers/utils/import_utils.py --wdir
pip install tf-keras
%runfile C:/Windows/System32/purple_env/Lib/site-packages/transformers/utils/import_utils.py --wdir
%runfile C:/nlpsentimentanalysis/untitled3.py --wdir

## ---(Tue Dec 10 01:38:12 2024)---
%runfile C:/nlpsentimentanalysis/bert.py --wdir
%runfile C:/nlpsentimentanalysis/bert.py --wdir

## ---(Tue Dec 10 04:42:46 2024)---
%runfile C:/nlpsentimentanalysis/bert.py --wdir
pip install scikit-learn
%runfile C:/nlpsentimentanalysis/bert.py --wdir

## ---(Thu Dec 12 08:48:19 2024)---
%runfile C:/Users/yanfr/untitled0.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/untitled1.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/exploratory-data-analysis.py --wdir

## ---(Fri Dec 13 06:37:46 2024)---
%runfile C:/medicaldiagnostics/scripts/python/exploratory-data-analysis.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/exploratory-data-analysis.py --wdir
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# load the data from CSV

df = pd.read_csv("med-diagnos-data-export.csv")

# plot histogram for age

plt.figure(figsize=(10,6))
plt.hist(df['age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# bar plot for primary condition distribution

plt.figure(figsize=(10,6))
sns.countplot(data=df, x='primarycondition', palette='viridis')
plt.title('Primary Condition Distribution')
plt.xlabel('Primary Condition')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()

# histogram for age

plt.figure(figsize=(10,6))
sns.histplot(df['age'], bins=20, kde=True, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# convert dosage to numeric and plot

df['dosage_in_mg'] = df['dosage_in_mg'].apply(pd.to_numeric, errors='coerce')

plt.figure(figsize=(10,6))
sns.histplot(df['dosage_in_mg'], bins=15, kde=True, color='lightgreen', edgecolor='black')
plt.title('Medication Dosage Distribution')
plt.xlabel('Dosage (mg)')
plt.ylabel('Frequency')
plt.show()

# boxplot for age by primary condition

plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='primarycondition', y='age', palette='Set2')
plt.title('Age Distribution by Primary Condition')
plt.xlabel('Primary Condition')
plt.ylabel('Age')
plt.xticks(rotation=45)
plt.show()


%runfile C:/medicaldiagnostics/scripts/python/exploratory-data-analysis.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/untitled0.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/untitled1.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/untitled2.py --wdir

## ---(Fri Dec 13 11:22:08 2024)---
%runfile C:/medicaldiagnostics/scripts/python/untitled0.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/untitled1.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/untitled0.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/untitled2.py --wdir
%runfile 'C:/medicaldiagnostics/scripts/python/extra scripts/untitled3.py' --wdir
%runfile C:/medicaldiagnostics/scripts/python/feature-engineering.py --wdir
%runfile 'C:/medicaldiagnostics/scripts/python/extra scripts/untitled3.py' --wdir
%runfile C:/medicaldiagnostics/scripts/python/feature-engineering.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/untitled4.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/untitled5.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/untitled6.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/untitled7.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/gradient-boosting.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/xgboost.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/xg-boost.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/xg-boost.py --wdir

## ---(Sun Dec 15 05:32:36 2024)---
%runfile C:/medicaldiagnostics/scripts/python/untitled0.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/untitled1.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/untitled1.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/untitled2.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/untitled3.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/untitled4.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/catboost-extratrees_regressor.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/catboost-extratrees_regressor.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/catboost-extratrees_regressor.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/untitled6.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/untitled7.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/plotting.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/untitled7.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/modeling.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/advanced-modeling.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/svr-modeling.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/untitled8.py --wdir
%runfile C:/medicaldiagnostics/scripts/python/untitled9.py --wdir
%runcell -i 0 C:/medicaldiagnostics/scripts/python/untitled9.py
%runfile C:/medicaldiagnostics/scripts/python/untitled9.py --wdir
%tb
%runfile C:/medicaldiagnostics/scripts/python/untitled9.py --wdir

## ---(Wed Dec 18 12:02:57 2024)---
%runfile C:/Users/yanfr/.spyder-py3/temp.py --wdir
%runfile C:/Users/yanfr/.spyder-py3/data-transformation.py --wdir
%runfile C:/Users/yanfr/.spyder-py3/untitled2.py --wdir
%runfile C:/Users/yanfr/.spyder-py3/untitled3.py --wdir
%runfile C:/Users/yanfr/.spyder-py3/untitled4.py --wdir
%runfile C:/Users/yanfr/.spyder-py3/untitled5.py --wdir
%runfile C:/Users/yanfr/.spyder-py3/baseline_models.py --wdir
%runfile C:/Users/yanfr/.spyder-py3/advanced_models.py --wdir
%runfile C:/Users/yanfr/.spyder-py3/model-training.py --wdir
%runfile C:/Users/yanfr/.spyder-py3/model-evaluation.py --wdir
%runfile C:/Users/yanfr/.spyder-py3/model-evaluation.py --wdir
%runfile C:/Users/yanfr/.spyder-py3/untitled9.py --wdir
%runfile C:/Users/yanfr/.spyder-py3/feature_importance_analysis.py --wdir
%runfile C:/Users/yanfr/.spyder-py3/residual_analysis.py --wdir
%runfile C:/Users/yanfr/.spyder-py3/model_saving_and_reporting.py --wdir
%runfile C:/Users/yanfr/.spyder-py3/untitled14.py --wdir
%runcell -i 0 C:/Users/yanfr/.spyder-py3/untitled13.py
%runfile C:/Users/yanfr/.spyder-py3/untitled13.py --wdir
%runfile C:/Users/yanfr/.spyder-py3/advanced_stats.py --wdir