# just made the file, but then run into trouble

import pandas as pd

df0 = pd.read_csv(r"ready_data/data_a0_encoded.csv")
df1 = pd.read_csv(r"ready_data/data_a1_encoded.csv")

print(df0.describe().T)

