import pandas as pd
import numpy as np
import joblib
import os

# ==========================================================
# ENGINEERING GUIDED AI OPTIMIZATION
# ==========================================================

print("=" * 70)
print("STEP 6 : ENGINEERING GUIDED AI OPTIMIZATION")
print("=" * 70)

os.makedirs("Engineering_AI", exist_ok=True)

# ==========================================================
# LOAD TRAINED MODEL
# ==========================================================

model = joblib.load("Model_Selection/Best_Model.pkl")

print("\nBest Model Loaded Successfully.")

# ==========================================================
# READ DATASET
# ==========================================================

df = pd.read_excel("Prepared_Data/Prepared_Dataset.xlsx")

max_ppi = df["PPI"].max()
min_ppi = df["PPI"].min()

print(f"\nTraining PPI Range : {min_ppi:.4f}  --->  {max_ppi:.4f}")

# ==========================================================
# FIXED VARIABLES
# ==========================================================
# Use values from your validated/base case

RR2_FIXED = 2.5
PRESSURE_FIXED = 1.4

# ==========================================================
# NUMBER OF CANDIDATES
# ==========================================================

N = 100000

np.random.seed(42)

# ==========================================================
# INTELLIGENT SAMPLING FUNCTION
# ==========================================================

def biased_sample(low, high, bias_low, bias_high, size):

    n_bias = int(size * 0.80)
    n_random = size - n_bias

    bias = np.random.uniform(bias_low, bias_high, n_bias)
    random = np.random.uniform(low, high, n_random)

    values = np.concatenate([bias, random])

    np.random.shuffle(values)

    return values

# ==========================================================
# GENERATE ENGINEERING FEASIBLE CONDITIONS
# ==========================================================

candidate = pd.DataFrame({

    "Boilup":

        biased_sample(
            0.35,
            0.59,
            0.45,
            0.58,
            N
        ),

    "Bottom Flow C2":

        biased_sample(
            0.06,
            0.09,
            0.075,
            0.09,
            N
        ),

    "RR2":

        RR2_FIXED,

    "Pressure C2":

        PRESSURE_FIXED,

    "Temp C1":

        biased_sample(
            180,
            240,
            220,
            240,
            N
        )

})

# ==========================================================
# ROUND VALUES
# ==========================================================

candidate = candidate.round({

    "Boilup":3,
    "Bottom Flow C2":3,
    "RR2":2,
    "Pressure C2":2,
    "Temp C1":0

})

candidate = candidate.drop_duplicates()

candidate.reset_index(drop=True, inplace=True)

print("\nUnique Candidate Conditions :", len(candidate))

# ==========================================================
# PREDICT
# ==========================================================

candidate["Predicted PPI"] = model.predict(candidate)

# ==========================================================
# REMOVE IMPOSSIBLE PREDICTIONS
# ==========================================================

candidate = candidate[
    (candidate["Predicted PPI"] >= min_ppi) &
    (candidate["Predicted PPI"] <= max_ppi)
]

candidate.reset_index(drop=True, inplace=True)

print("Physically Feasible Predictions :", len(candidate))

# ==========================================================
# SORT
# ==========================================================

candidate = candidate.sort_values(
    by="Predicted PPI",
    ascending=False
)

candidate.reset_index(drop=True, inplace=True)

# ==========================================================
# SAVE RESULTS
# ==========================================================

best = candidate.head(1)

top5 = candidate.head(5)

top20 = candidate.head(20)

top100 = candidate.head(100)

candidate.to_excel(
    "Engineering_AI/All_AI_Predictions.xlsx",
    index=False
)

best.to_excel(
    "Engineering_AI/Best_Operating_Condition.xlsx",
    index=False
)

top5.to_excel(
    "Engineering_AI/Top5_DWSIM_Validation.xlsx",
    index=False
)

top20.to_excel(
    "Engineering_AI/Top20_AI_Operating_Conditions.xlsx",
    index=False
)

top100.to_excel(
    "Engineering_AI/Top100_AI_Operating_Conditions.xlsx",
    index=False
)

# ==========================================================
# DISPLAY
# ==========================================================

print("\n")
print("=" * 70)
print("BEST OPERATING CONDITION")
print("=" * 70)

print(best)

print("\nHighest Predicted PPI :",
      round(best.iloc[0]["Predicted PPI"],4))

print("\nTop 5 Operating Conditions")
print(top5)

print("\nResults Saved Successfully.")

print("=" * 70)