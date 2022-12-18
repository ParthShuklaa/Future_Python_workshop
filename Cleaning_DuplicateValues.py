import pandas as pd
df = pd.read_csv('student.csv')
df.drop_duplicates(inplace=True)
print(df.to_string())
#All those rows with same values will be removed 