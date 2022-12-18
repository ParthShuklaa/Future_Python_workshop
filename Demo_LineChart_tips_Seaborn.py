import seaborn as sns
import matplotlib.pyplot as plt

#loading data
data = sns.load_dataset("tips")
#drawing lineplot for tips databased on gender
sns.lineplot(x="total_bill",y="size",hue ="sex",style="sex",data= data)
plt.show()