import pandas as pd

data = pd.read_csv('gielda.csv', sep=",")

print(data)
df = pd.DataFrame(data)

print("---------------------------------------------")
for column in df.columns:
    print(df[column].value_counts())
    print("\n")
print("---------------------------------------------")


unique = df.nunique()
