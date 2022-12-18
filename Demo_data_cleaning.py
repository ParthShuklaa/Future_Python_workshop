import pandas
df = pandas.read_csv('student.csv')#reading from  File
#print(df)
newDF = df.dropna()#It will return rows with no empty cells
print("___________________________________________________")
print(newDF)
print("Mean of the marks is:")
marks_mean = newDF["mark"].mean()#calculating mean of Marks for student csv data
marks_median = newDF["mark"].median()
print(marks_mean)
print("Median of the mark is :",marks_median)
print("Mode of the mark is: ",newDF["mark"].mode())