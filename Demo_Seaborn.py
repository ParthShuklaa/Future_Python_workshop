#Step:1 INstalling python package
import seaborn as sns
import matplotlib.pyplot as plt
#Step:2 Distplot() - Distribution plots, it takes as input an array and plots a curve correposnding
# to the distribution of points in the array
sns.distplot([0,1,2,3,4,5])
plt.show()