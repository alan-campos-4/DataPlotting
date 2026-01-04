import pandas as pd
import matplotlib.pyplot as plt




data = pd.read_csv('datasheets/albums.csv', on_bad_lines='warn')
df_data = pd.DataFrame(data)




def album_analysis(view, update, graph):

	# ==============
	# View options
	# ==============
	if view:

		print("1) View full table.")
		print("2) View albums by group.") ###
		print("3) View albums by genre.") ###
		print("4) View albums by group and year listened to.") ###
		print("5) View albums by month listened to.") ###
		print("6) View albums by group and five-year period released.") ###
		try:
			opt = input("Select an option: ")
			opti = int(opt)
			if opti in range(1,7):
				if opti==1:
					display_full_table()
				if opti==2:
					display_by_group(graph)
				if opti==3:
					display_by_genre(graph)
				if opti==4:
					display_by_listen_year(graph)
				if opti==5:
					display_by_listen_month(graph)
				else:
					display_by_year_period(graph)
				
			else:
				print("Option not valid.")
		except ValueError:
			print("Option not valid.")
	
	
	# ==============
	# Update the datatable
	# ==============
	else:
		print("CRUD")




## ----------
## 1) View the full datatable.
## ----------
def display_full_table():
	max_rows, max_cols = df_data.shape
	pd.set_option('display.max_rows', max_rows)
	print(df_data)




## ----------
## 2) View albums by group.
## ----------
def display_by_group(graph):
	print('----------\nAlbums by group: ')
	df1 = df.pivot_table(index=['Group'], aggfunc={'Group': 'count'})
	df1 = df1.rename(columns={'Group': 'Group Count'})
	df1 = df1.reset_index()
	df1 = df1.sort_values(by=['Group Count'], ascending=False)
	print(df1)

	## Pie chart
	df1.plot.pie(y='Group Count')
	plt.show()




## ----------
## 3) View albums by genre.
## ----------
def display_by_genre(graph):
	print("...")




## ----------
## 4) View albums by group and year listened to.
## ----------
def display_by_listen_year(graph):
	print("...")




## ----------
## 5) View albums by month listened to.
## ----------
def display_by_listen_month(graph):
	print("...")




## ----------
## 6) View albums by group and five-year period released.
## ----------
def display_by_year_period(graph):
	print("...")



