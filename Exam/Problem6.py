import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("anomalies.csv")


limit = 6


plt.scatter(range(189 - len(df[df['value'] > limit]))  , df[df['value'] < limit])
plt.scatter(df[df['value'] >limit].index, df[df['value'] > limit], color='r')



plt.xlabel("Index")
plt.ylabel("Values")

plt.show()

