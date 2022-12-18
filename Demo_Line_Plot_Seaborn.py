import seaborn as sns
import matplotlib.pyplot as plt

#loading dataset present inside seaborn package
data = sns.load_dataset("iris")
#drawlineplot
sns.lineplot(x= "sepal_length", y="sepal_width",data=data)
#Showing graph
plt.show()