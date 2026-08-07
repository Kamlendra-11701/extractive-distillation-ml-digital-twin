import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ==========================================================
# READ DATASET
# ==========================================================

df = pd.read_excel("ML_Dataset.xlsx")

print("\n================ DATASET INFORMATION ================\n")

print(df.info())

print("\nDataset Shape :", df.shape)

# ==========================================================
# CREATE OUTPUT FOLDER
# ==========================================================

os.makedirs("EDA_Results", exist_ok=True)

# ==========================================================
# MISSING VALUES
# ==========================================================

missing = df.isnull().sum()

print("\n================ MISSING VALUES ================\n")
print(missing)

missing.to_excel("EDA_Results/Missing_Values.xlsx")

# ==========================================================
# DUPLICATE ROWS
# ==========================================================

duplicates = df.duplicated().sum()

print("\nDuplicate Rows :", duplicates)

# ==========================================================
# DESCRIPTIVE STATISTICS
# ==========================================================

statistics = df.describe()

statistics.to_excel("EDA_Results/Statistics.xlsx")

print("\nStatistics saved.")

# ==========================================================
# CORRELATION MATRIX
# ==========================================================

corr = df.corr(numeric_only=True)

corr.to_excel("EDA_Results/Correlation.xlsx")

plt.figure(figsize=(12,10))

plt.imshow(corr,
           cmap="coolwarm",
           interpolation='nearest')

plt.colorbar()

plt.xticks(range(len(corr.columns)),
           corr.columns,
           rotation=90)

plt.yticks(range(len(corr.columns)),
           corr.columns)

plt.title("Correlation Matrix")

plt.tight_layout()

plt.savefig("EDA_Results/Correlation_Matrix.png",dpi=300)

plt.close()

# ==========================================================
# HISTOGRAMS
# ==========================================================

os.makedirs("EDA_Results/Histograms", exist_ok=True)

for column in df.columns:

    if np.issubdtype(df[column].dtype, np.number):

        plt.figure(figsize=(6,4))

        plt.hist(df[column],
                 bins=10)

        plt.title(column)

        plt.xlabel(column)

        plt.ylabel("Frequency")

        plt.tight_layout()

        plt.savefig(f"EDA_Results/Histograms/{column}.png",
                    dpi=300)

        plt.close()

print("Histograms Generated.")

# ==========================================================
# BOXPLOTS
# ==========================================================

os.makedirs("EDA_Results/Boxplots", exist_ok=True)

for column in df.columns:

    if np.issubdtype(df[column].dtype, np.number):

        plt.figure(figsize=(4,6))

        plt.boxplot(df[column])

        plt.title(column)

        plt.tight_layout()

        plt.savefig(f"EDA_Results/Boxplots/{column}.png",
                    dpi=300)

        plt.close()

print("Boxplots Generated.")

# ==========================================================
# SCATTER PLOTS
# ==========================================================

inputs = [
    "Boilup",
    "Bottom Flow C2",
    "RR2",
    "Pressure C2",
    "Temp C1"
]

outputs = [
    "Ethanol Purity",
    "Ethanol Recovery",
    "EG Recovery",
    "Total Energy",
    "PPI"
]

os.makedirs("EDA_Results/ScatterPlots", exist_ok=True)

for x in inputs:

    for y in outputs:

        plt.figure(figsize=(6,4))

        plt.scatter(df[x],df[y])

        plt.xlabel(x)

        plt.ylabel(y)

        plt.title(f"{x} vs {y}")

        plt.tight_layout()

        plt.savefig(f"EDA_Results/ScatterPlots/{x}_vs_{y}.png",
                    dpi=300)

        plt.close()

print("Scatter plots Generated.")

# ==========================================================
# OUTLIER DETECTION USING IQR
# ==========================================================

outlier_summary = []

for column in df.columns:

    if np.issubdtype(df[column].dtype,np.number):

        Q1 = df[column].quantile(0.25)

        Q3 = df[column].quantile(0.75)

        IQR = Q3-Q1

        lower = Q1-1.5*IQR

        upper = Q3+1.5*IQR

        outliers = df[(df[column]<lower)|
                      (df[column]>upper)]

        outlier_summary.append([

            column,

            len(outliers)

        ])

outlier_df = pd.DataFrame(outlier_summary,
                          columns=["Variable",
                                   "No of Outliers"])

outlier_df.to_excel("EDA_Results/Outlier_Summary.xlsx",
                    index=False)

print("Outlier Summary Saved.")

# ==========================================================
# FINISH
# ==========================================================

print("\n=======================================")
print("EDA COMPLETED SUCCESSFULLY")
print("=======================================")

print("\nFiles Generated inside EDA_Results folder.")