import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif, mutual_info_classif
from sklearn.impute import SimpleImputer

# file paths

input_file = "C:/data/feature_enhanced_mortality_data.csv"
output_file = "C:/data/selected_features_mortality_data.csv"

# load the dataset

print("loading dataset...")
data = pd.read_csv(input_file)

# inspect dataset

print("dataset shape:", data.shape)
print("columns:", list(data.columns))

# define features (X) and target variable (y)

features = ["age", "co_morbidity_count", "socioeconomic_index", "age_squared", "co_morbidity_per_age",
            "socio_co_morbidity_interaction", "log_socioeconomic_index", "high_risk_flag", "cause_of_death_frequency"]
target = "infant_death_flag"

X = data[features]
y = data[target]

# handle missing values by imputing with mean

print("handling missing values...")
imputer = SimpleImputer(strategy="mean")
X = pd.DataFrame(imputer.fit_transform(X), columns=features)

# apply SelectKBest (ANOVA F-value)

print("selecting best features using ANOVA F-value...")
selector_anova = SelectKBest(score_func=f_classif, k=5)
X_anova = selector_anova.fit_transform(X, y)

# print scores for each feature

anova_scores = selector_anova.scores_
selected_features_anova = [features[i] for i in selector_anova.get_support(indices=True)]
print("ANOVA-selected features:", selected_features_anova)

# apply SelectKBest (Mutual Information)

print("selecting best features using Mutual Information...")
selector_mi = SelectKBest(score_func=mutual_info_classif, k=5)
X_mi = selector_mi.fit_transform(X, y)

# print scores for each feature

mi_scores = selector_mi.scores_
selected_features_mi = [features[i] for i in selector_mi.get_support(indices=True)]
print("Mutual Information-selected features:", selected_features_mi)

# save selected features (ANOVA) to a new dataset

selected_features = selected_features_anova
selected_data = data[selected_features + [target]]
selected_data.to_csv(output_file, index=False)
print(f"dataset with selected features saved to {output_file}")
