

import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
print(df)

print("\nShape of dataset : ",df.shape)

print("\n\n Top rows of the dataset : \n",df.head())

print("\n\n Random rows from the dataset : \n",df.sample(5))

print("\n\n Number of columns : ",len(df.columns))
print("\n\n Names of columns : ",df.columns.tolist())