import pprint
import json
import pandas as pd


data = {
  "calories": [420, 380, 390,44,75],
  "duration": [50, 40, 45,62,66]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)