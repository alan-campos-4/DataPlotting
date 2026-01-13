import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np


data = pd.read_csv('datasheets/books.csv', on_bad_lines='warn')
df_data = pd.DataFrame(data)


# ==============
# Display the datatable
# ==============

def book_view(graph, save):
	print("1) View full table.")
	print("2) Display spending over time.")
	print("3) Display acquisition over time.")
	"""
	print("3) Display quantity by year.")
	print("3) Display reading by year.")
	print("3) Display reading status.")
	print("3) Display by genre.")
	print("3) Display by location.")
	print("3) Display by country.")
	print("3) Display by format.")
	"""
	try:
		opt = input("Select an option: ")
		opti = int(opt)
		if opti in range(1,4):
			
			## View the full datatable
			if opti==1:
				display_full_table()
			## View the pivot tables and their graphs.
			elif opti==2 or opti==3:
				display_table(opti, graph)
			
		else:
			print("Option not valid.")
	except ValueError:
		print("Option not valid.")


# ==============
# Update the datatable
# ==============

def book_db():
	print("CRUD")






## ----------
## 1) View the full datatable.
## ----------
def display_full_table():
	max_rows, max_cols = df_data.shape
	pd.set_option('display.max_rows', max_rows)
	print(df_data)




## ----------
## 2) View book spending
## 3) View book acquisitions
## ----------
def display_table(opti, graph):
	#Append the 'Year' column for grouping by converting the 'Date' column to datetime, and extracting the year
	df_data['Date'] = pd.to_datetime(df_data['Date'])
	df_data['Year'] = df_data['Date'].dt.year
	
	#Assign new variables based on the option
	df = df1()
	title = title1
	ylabel = ylabel1
	if opti==3:
		df = df2()
		title = title2
		ylabel = ylabel2
	
	#Collapse the data from multiple columns to 'Others' column, and then delete them
	df['Others'] = df[['Dad','Gift','Mom']].sum(axis=1) #Grandma not in index
	df = df.drop(['Dad','Gift','Mom'], axis=1)
	#Create 'Total' column
	df['Total'] = df.sum(axis=1)
	#Show the table
	print('\n',title,':\n----------')
	print(df)
	
	if graph:	##If the option to show the graph is selected
		#Plot the columns as bars
		fig, ax = plt.subplots()
		df.plot(
			y=['Myself','Wallet','Others'],
			kind='bar',
			ax=ax,
			color=['blue','red','green'],
			label=['Myself','Wallet','Others']
		)
		#Plot the Total line using the SAME x positions
		ax.plot(
			range(len(df)),
			df['Total'],
			color='black',
			linewidth=2.5,
			zorder=10,
			marker='o',
			label='Total',
		)
		#Other properties of the graph
		ax.set_title(title)
		ax.set_xlabel('Year')
		ax.set_ylabel(ylabel)
		ax.legend(loc='upper left')
		
		#Show the plot
		plt.tight_layout()
		plt.show()
## ----------
## Parameters.
## ----------
def df1():
	return df_data.pivot_table(index='Year', columns='Paid', values='Price', aggfunc='sum')
def df2():
	return df_data.pivot_table(index='Year', columns='Paid', values='Price', aggfunc='count')
title1 = "Book Spending by Paid category over Time"
title2 = "Books Acquired by Paid category over Time"
ylabel1 = 'Spending (€)'
ylabel2 = 'Nº of Books'





