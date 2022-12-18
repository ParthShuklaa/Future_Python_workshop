#Step 1: importing package
import pandas as pd
#step 2: Creating data frame that will read data from csv file
df = pd.read_csv('student.csv')
#step 3: display data
print(df.to_string())