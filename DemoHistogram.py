import matplotlib.pyplot as plt
import pandas as pd
import sys
df = pd.read_csv('data.csv')
df["Duration"].plot(kind = 'pie')
plt.show()





















