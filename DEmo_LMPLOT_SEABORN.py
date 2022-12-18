import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="ticks")

#loading the dataset
df = sns.load_dataset("anscombe")
#showing result of alinear regression
sns.lmplot(x="x",y="y", data=df)
plt.show()
