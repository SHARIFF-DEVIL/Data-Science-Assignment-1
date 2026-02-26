import pandas as pd
import numpy as np

file_path = "Quote-Equity-HDFC-EQ-01-08-2018-to-30-07-2020.csv"
df = pd.read_csv(file_path)

df.columns = df.columns.str.strip()

cols = [
    "OPEN","HIGH","LOW","PREV. CLOSE","ltp","close",
    "vwap","52W H","52W L","VOLUME","VALUE","No of trades"
]

for c in cols:
    df[c] = pd.to_numeric(df[c].astype(str).str.replace(',', ''), errors='coerce')

numeric_df = df[cols]

stats_table = pd.DataFrame({
    "Mean": numeric_df.mean(),
    "Median": numeric_df.median(),
    "Mode": numeric_df.mode().iloc[0],
    "Variance": numeric_df.var(),
    "Standard Deviation": numeric_df.std()
}).round(6)

print("\n=========== STOCK MARKET STATISTICAL TABLE ===========\n")
print(stats_table)


data_np = numeric_df.to_numpy()

print("\n=========== NUMPY OPERATIONS ===========\n")

print("Min values:\n", np.nanmin(data_np, axis=0))
print("Max values:\n", np.nanmax(data_np, axis=0))

print("\nPercentiles:\n", np.nanpercentile(data_np, [25,50,75], axis=0))

corr_matrix = np.corrcoef(np.nan_to_num(data_np).T)
print("\nCorrelation Matrix Shape:", corr_matrix.shape)

mean = np.nanmean(data_np, axis=0)
std = np.nanstd(data_np, axis=0)
zscore_data = (data_np - mean) / std

print("\nZ-score sample (first 5 rows):\n", zscore_data[:5])
