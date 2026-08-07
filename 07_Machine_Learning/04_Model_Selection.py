import pandas as pd
import joblib
import os

from sklearn.model_selection import KFold, cross_val_score

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import ExtraTreesRegressor

# ==========================================================
# MODEL SELECTION
# ==========================================================

print("="*65)
print("STEP 4 : MODEL SELECTION")
print("="*65)

os.makedirs("Model_Selection", exist_ok=True)

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
# CROSS VALIDATION
# ==========================================================

cv = KFold(

    n_splits=5,

    shuffle=True,

    random_state=42

)

# ==========================================================
# MODELS
# ==========================================================

models = {

    "Linear Regression":

        Pipeline([

            ("Scaler",StandardScaler()),

            ("Model",LinearRegression())

        ]),

    "Random Forest":

        RandomForestRegressor(

            n_estimators=300,

            random_state=42

        ),

    "Gradient Boosting":

        GradientBoostingRegressor(

            random_state=42

        ),

    "Extra Trees":

        ExtraTreesRegressor(

            n_estimators=300,

            random_state=42

        )

}

# ==========================================================
# EVALUATION
# ==========================================================

results=[]

best_score=-100

best_model = models["Linear Regression"]
best_name = "Linear Regression"
best_score = -9999

best_name=""

for name,model in models.items():

    print(f"\nTraining {name}...")

    scores=cross_val_score(

        model,

        X,

        y,

        cv=cv,

        scoring="r2"

    )

    mean_score=scores.mean()

    std_score=scores.std()

    results.append({

        "Model":name,

        "Mean R2":mean_score,

        "Std Dev":std_score

    })

    print("Fold Scores :",scores)

    print("Average R2 :",round(mean_score,4))

    print("Std Dev :",round(std_score,4))

    if mean_score>best_score:

        best_score=mean_score

        best_model=model

        best_name=name

# ==========================================================
# TRAIN BEST MODEL ON COMPLETE DATASET
# ==========================================================

best_model.fit(X,y)

joblib.dump(

    best_model,

    "Model_Selection/Best_Model.pkl"

)

# ==========================================================
# SAVE RESULTS
# ==========================================================

results_df=pd.DataFrame(results)

results_df=results_df.sort_values(

    by="Mean R2",

    ascending=False

)

results_df.to_excel(

    "Model_Selection/Model_Comparison.xlsx",

    index=False

)

print()

print("="*65)

print("FINAL MODEL RANKING")

print("="*65)

print(results_df)

print()

print("BEST MODEL :",best_name)

print("BEST CROSS VALIDATED R2 :",round(best_score,4))

print()

print("Best model saved as Best_Model.pkl")

print("="*65)