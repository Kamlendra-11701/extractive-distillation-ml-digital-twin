import pandas as pd
import numpy as np
import os

# ============================================================
# DATASET PREPARATION
# Chemical Engineering ML Project
# ============================================================

print("="*60)
print("STEP 2 : DATASET PREPARATION")
print("="*60)

# ============================================================
# CREATE OUTPUT FOLDER
# ============================================================

os.makedirs("Prepared_Data", exist_ok=True)

# ============================================================
# READ ORIGINAL DATASET
# ============================================================

df = pd.read_excel("ML_Dataset.xlsx")

print("\nOriginal Dataset Shape :", df.shape)

# ============================================================
# REMOVE LEADING/TRAILING SPACES FROM COLUMN NAMES
# ============================================================

df.columns = df.columns.str.strip()

# ============================================================
# VERIFY REQUIRED COLUMNS
# ============================================================

required_columns = [

    "Run",
    "Boilup",
    "Bottom Flow C2",
    "RR2",
    "Pressure C2",
    "Temp C1",

    "Ethanol Purity",
    "Ethanol Recovery",
    "EG Recovery",
    "Total Energy",
    "PPI"

]

missing = []

for col in required_columns:

    if col not in df.columns:

        missing.append(col)

if len(missing) > 0:

    print("\nERROR")
    print("Missing Columns :")

    for col in missing:

        print(col)

    raise SystemExit

print("\nAll required columns found.")

# ============================================================
# REMOVE DUPLICATES
# ============================================================

duplicates = df.duplicated().sum()

print("\nDuplicate Rows :", duplicates)

df = df.drop_duplicates()

# ============================================================
# REMOVE MISSING VALUES
# ============================================================

print("\nMissing Values Before Cleaning")

print(df.isnull().sum())

df = df.dropna()

print("\nMissing Values After Cleaning")

print(df.isnull().sum())

# ============================================================
# RESET INDEX
# ============================================================

df = df.reset_index(drop=True)

# ============================================================
# CONVERT DATATYPES
# ============================================================

numeric_columns = [

    "Boilup",
    "Bottom Flow C2",
    "RR2",
    "Pressure C2",
    "Temp C1",

    "Ethanol Purity",
    "Ethanol Recovery",
    "EG Recovery",
    "Total Energy",
    "PPI"

]

for col in numeric_columns:

    df[col] = pd.to_numeric(df[col])

# ============================================================
# SORT DATASET
# ============================================================

df = df.sort_values("Run")

# ============================================================
# RESET INDEX AGAIN
# ============================================================

df = df.reset_index(drop=True)

# ============================================================
# BASIC INFORMATION
# ============================================================

print("\nPrepared Dataset Shape :", df.shape)

print("\nData Types")

print(df.dtypes)

# ============================================================
# SAVE PREPARED DATASET
# ============================================================

output_file = "Prepared_Data/Prepared_Dataset.xlsx"

df.to_excel(output_file,index=False)

print("\nPrepared dataset saved.")

# ============================================================
# SAVE INPUT FEATURES
# ============================================================

inputs = df[[
    "Boilup",
    "Bottom Flow C2",
    "RR2",
    "Pressure C2",
    "Temp C1"
]]

inputs.to_excel(
    "Prepared_Data/Input_Features.xlsx",
    index=False
)

# ============================================================
# SAVE OUTPUT FEATURES
# ============================================================

outputs = df[[
    "Ethanol Purity",
    "Ethanol Recovery",
    "EG Recovery",
    "Total Energy",
    "PPI"
]]

outputs.to_excel(
    "Prepared_Data/Output_Features.xlsx",
    index=False
)

# ============================================================
# SAVE FEATURE SUMMARY
# ============================================================

summary = pd.DataFrame({

    "Feature":[

        "Boilup",
        "Bottom Flow C2",
        "RR2",
        "Pressure C2",
        "Temp C1",

        "Ethanol Purity",
        "Ethanol Recovery",
        "EG Recovery",
        "Total Energy",
        "PPI"

    ],

    "Minimum":[

        df["Boilup"].min(),
        df["Bottom Flow C2"].min(),
        df["RR2"].min(),
        df["Pressure C2"].min(),
        df["Temp C1"].min(),

        df["Ethanol Purity"].min(),
        df["Ethanol Recovery"].min(),
        df["EG Recovery"].min(),
        df["Total Energy"].min(),
        df["PPI"].min()

    ],

    "Maximum":[

        df["Boilup"].max(),
        df["Bottom Flow C2"].max(),
        df["RR2"].max(),
        df["Pressure C2"].max(),
        df["Temp C1"].max(),

        df["Ethanol Purity"].max(),
        df["Ethanol Recovery"].max(),
        df["EG Recovery"].max(),
        df["Total Energy"].max(),
        df["PPI"].max()

    ]

})

summary.to_excel(
    "Prepared_Data/Feature_Ranges.xlsx",
    index=False
)

print("\nFeature ranges saved.")

# ============================================================
# FINISH
# ============================================================

print("\n" + "="*60)
print("DATASET PREPARATION COMPLETED SUCCESSFULLY")
print("="*60)