import pandas as pd

df = pd.read_csv("results.csv")

print(df)

for index, row in df.iterrows():
    if row["status_code"] == 200:
        print(f"PASS: {row['prompt']}")
    else:
        print(f"FAIL: {row['prompt']}")
if "json" in row["result"]:
    print("Schema valid")