import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
sns.set(style = "white")
# Generating a random univariate dataset
rs = np.random.RandomState(10)
d = rs.normal(size=100)

# plotting a simple histogram
sns.displot(d,kde=True, color='m')
plt.show()
