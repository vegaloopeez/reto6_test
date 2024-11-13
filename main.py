import pandas as pd
import os

DATASET= os.path.join("prueba.csv")

df=pd.read_csv(DATASET)

print(df)
