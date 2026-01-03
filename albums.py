import pandas as pd
import matplotlib.pyplot as plt




def album_analysis():
	data = pd.read_csv('datasheets/AlbumLog_corrected.csv', on_bad_lines='warn')
	df = pd.DataFrame(data)
	#print('----------\nData Table: ')
	#print(df)


	##### Albums by group
	## Table
	print('----------\nAlbums by group: ')
	df1 = df.pivot_table(index=['Group'], aggfunc={'Group': 'count'})
	df1 = df1.rename(columns={'Group': 'Group Count'})
	df1 = df1.reset_index()
	df1 = df1.sort_values(by=['Group Count'], ascending=False)
	print(df1)

	## Pie chart
	df1.plot.pie(y='Group Count')
	plt.show()
