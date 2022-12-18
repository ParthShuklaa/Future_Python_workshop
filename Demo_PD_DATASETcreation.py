#Step1: import package
import pandas
#Step2: Create DataSet
mydataset = {
    'cars':["BMW","VOLVO","FERARI"],
    'Model':[2020,2019,2001],
    'Colors':["Red","Yellow","Black"],
    'sales':[120,110,90]

}
#Step3: Storing DataSet as DataFrame and provinding index
myDF = pandas.DataFrame(mydataset,index=["First Car","Second Car","Third Car"])
#Step4: Displaying dataFrame
print(myDF)
#Step5: Locating a Row
#print(myDF.loc[1])#Extracting one row - series
#print(myDF.loc[[1,2]])#Extracting Two rows - Dataframe
print(myDF.loc["Second Car"])

