import pandas as pd
import numpy as np
import joblib
import os

# ============================================================
# STEP 5 : AI OPTIMIZATION
# ============================================================

print("="*70)
print("STEP 5 : AI ASSISTED PROCESS OPTIMIZATION")
print("="*70)

os.makedirs("AI_Optimization", exist_ok=True)

# ============================================================
# LOAD TRAINED MODEL
# ============================================================

model = joblib.load("Model_Selection/Best_Model.pkl")

print("\nBest Model Loaded Successfully.")

# ============================================================
# NUMBER OF CANDIDATES
# ============================================================

N = 100000

np.random.seed(42)

# ============================================================
# GENERATE NEW OPERATING CONDITIONS
# ============================================================

candidate = pd.DataFrame({

    "Boilup":

        np.random.uniform(0.35,0.59,N),

    "Bottom Flow C2":

        np.random.uniform(0.06,0.09,N),

    "RR2":

        np.random.uniform(1.0,3.0,N),

    "Pressure C2":

        np.random.uniform(0.8,2.0,N),

    "Temp C1":

        np.random.uniform(180,240,N)

})
candidate = candidate.round({

    "Boilup":3,
    "Bottom Flow C2":3,
    "RR2":2,
    "Pressure C2":2,
    "Temp C1":0

})

candidate = candidate.drop_duplicates()

candidate = candidate.reset_index(drop=True)

# ============================================================
# ENGINEERING CONSTRAINTS
# ============================================================

candidate = candidate[

    (candidate["Boilup"]>=0.35)&
    (candidate["Boilup"]<=0.59)&

    (candidate["Bottom Flow C2"]>=0.06)&
    (candidate["Bottom Flow C2"]<=0.09)&

    (candidate["RR2"]>=1.0)&
    (candidate["RR2"]<=3.0)&

    (candidate["Pressure C2"]>=0.8)&
    (candidate["Pressure C2"]<=2.0)&

    (candidate["Temp C1"]>=180)&
    (candidate["Temp C1"]<=240)

]

candidate = candidate.reset_index(drop=True)

print("\nFeasible Operating Conditions :",len(candidate))

# ============================================================
# PREDICT PPI
# ============================================================

candidate["Predicted PPI"] = model.predict(candidate)

# ============================================================
# SORT
# ============================================================

candidate = candidate.sort_values(

    by="Predicted PPI",

    ascending=False

)

candidate = candidate.reset_index(drop=True)

# ============================================================
# TOP 20
# ============================================================

top100 = candidate.head(100)

top20 = candidate.head(20)

best = candidate.iloc[[0]]

# ============================================================
# SAVE
# ============================================================

top100.to_excel(

    "AI_Optimization/Top100_AI_Operating_Conditions.xlsx",

    index=False

)

top20.to_excel(

    "AI_Optimization/Top20_AI_Operating_Conditions.xlsx",

    index=False

)

best.to_excel(

    "AI_Optimization/Best_AI_Operating_Condition.xlsx",

    index=False

)

candidate.to_excel(

    "AI_Optimization/All_AI_Predictions.xlsx",

    index=False

)

# ============================================================
# DISPLAY
# ============================================================

print("\n")
print("="*70)
print("TOP 20 AI RECOMMENDED OPERATING CONDITIONS")
print("="*70)

print(top20)

print("\nHighest Predicted PPI :",
      round(top20.iloc[0]["Predicted PPI"],4))

print("\nResults Saved.")

print("="*70)