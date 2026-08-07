import pandas as pd
import matplotlib.pyplot as plt
import os

from sklearn.ensemble import RandomForestRegressor

# ==========================================================
# FEATURE IMPORTANCE ANALYSIS
# ==========================================================

print("=" * 60)
print("STEP 3 : FEATURE IMPORTANCE")
print("=" * 60)

os.makedirs("Feature_Importance", exist_ok=True)

# ==========================================================
# READ DATA
# ==========================================================

df = pd.read_excel("Prepared_Data/Prepared_Dataset.xlsx")

# ==========================================================
# INPUTS
# ==========================================================

X = df[[
    "Boilup",
    "Bottom Flow C2",
    "RR2",
    "Pressure C2",
    "Temp C1"
]]

# ==========================================================
# TARGET
# ==========================================================

y = df["PPI"]

# ==========================================================
# RANDOM FOREST
# ==========================================================

model = RandomForestRegressor(

    n_estimators=500,

    random_state=42

)

model.fit(X, y)

importance = model.feature_importances_

# ==========================================================
# CREATE TABLE
# ==========================================================

importance_df = pd.DataFrame({

    "Feature": X.columns,

    "Importance": importance

})

importance_df = importance_df.sort_values(

    by="Importance",

    ascending=False

)

importance_df.reset_index(drop=True, inplace=True)

# ==========================================================
# DISPLAY
# ==========================================================

print()

print(importance_df)

# ==========================================================
# SAVE EXCEL
# ==========================================================

importance_df.to_excel(

    "Feature_Importance/Feature_Importance.xlsx",

    index=False

)

# ==========================================================
# BAR CHART
# ==========================================================

plt.figure(figsize=(9,6))

plt.bar(

    importance_df["Feature"],

    importance_df["Importance"]

)

plt.title("Feature Importance")

plt.xlabel("Input Variable")

plt.ylabel("Importance Score")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig(

    "Feature_Importance/Feature_Importance.png",

    dpi=300

)

plt.show()

# ==========================================================
# PERCENTAGE
# ==========================================================

importance_df["Importance (%)"] = (

    importance_df["Importance"]

    /

    importance_df["Importance"].sum()

) * 100

importance_df.to_excel(

    "Feature_Importance/Feature_Importance_Percentage.xlsx",

    index=False

)

print()

print("=" * 60)

print("FEATURE IMPORTANCE COMPLETED")

print("=" * 60)