import pandas as pd
import matplotlib.pyplot as plt
"""
df = pd.read_csv('data.csv')

#df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
df["Duration"].plot(kind = 'hist')

plt.show()
"""

df = pd.DataFrame({
	'mass': [0.330, 4.87 , 5.97],
	'radius': [2439.7, 6051.8, 6378.1]},
	index=['Mercury', 'Venus', 'Earth'])
print(df)
df.plot.pie(y='mass', figsize=(5, 5))
plt.show()
