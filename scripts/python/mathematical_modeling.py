import sympy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# file paths

dataset_path = "C:/data/selected_features_mortality_data.csv"

# load dataset

print("loading dataset...")
data = pd.read_csv(dataset_path)

# symbolic computation: deriving a formula for the relationship between age and infant death flag

print("performing symbolic computation...")
age, co_morbidity, socioeconomic, infant_flag = sp.symbols("age co_morbidity socioeconomic infant_flag")
relationship = sp.Eq(infant_flag, age * co_morbidity + socioeconomic)
print("derived relationship:")
sp.pprint(relationship)

# numerical verification

print("performing numerical verification...")
x = data["age"]
y = data["infant_death_flag"]
fit = np.polyfit(x, y, 1)  # simple linear regression for verification
print(f"numerical relationship: y = {fit[0]:.4f} * x + {fit[1]:.4f}")

# plot verification

plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.5, label="Data Points")
plt.plot(x, np.polyval(fit, x), color="red", label=f"y = {fit[0]:.4f} * x + {fit[1]:.4f}")
plt.title("Age vs Infant Death Flag")
plt.xlabel("Age")
plt.ylabel("Infant Death Flag")
plt.legend()
plt.tight_layout()
plt.show()
