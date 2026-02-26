import pandas as pd

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