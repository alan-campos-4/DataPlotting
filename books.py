import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np


data = pd.read_csv('datasheets/spending_books.csv', on_bad_lines='warn')
df = pd.DataFrame(data)


def book_analysis():

	print("1) View full table.")
	print("2) View book spending.")
	print("3) View book acquisition.")
	try:
		opt = input("Select an option: ")
		opti = int(opt)
		if opti in range(1,4):
			#Change the datatype of the Date column
			df['Date'] = pd.to_datetime(df['Date'])
			#Add the the Year column for sorting
			df['Year'] = df['Date'].dt.year


			if opti==1:
				max_rows, max_cols = df.shape
				pd.set_option('display.max_rows', max_rows)
				print(df)


			## Books spending over time: group by Date, for all values of Paid, show cost.
			elif opti==2:
				title = 'Book Spending by Paid category over Time'
				df_spend = df.pivot_table(
					index='Year',
					columns='Paid',
					values='Cost',
					aggfunc='sum'
				)
				
				#Create 'others' column
				df_spend['Others'] = df_spend[['Dad','Gift','Grandma','Mom']].sum(axis=1)
				#Delete not used columns
				df_spend = df_spend.drop(['Dad','Gift','Grandma','Mom'], axis=1)
				#Create 'Total' column
				df_spend['Total'] = df_spend.sum(axis=1)
				
				#Plot the columns as bars
				fig, ax = plt.subplots()
				df_spend.plot(
					y=['Myself','Wallet','Others'],
					kind='bar',
					ax=ax,
					color=['blue','red','green'],
					label=['Myself','Wallet','Others']
				)
				#Plot the Total line using the SAME x positions
				ax.plot(
					range(len(df_spend)),
					df_spend['Total'],
					color='black',
					linewidth=2.5,
					zorder=10,
					marker='o',
					label='Total',
				)
				#Other properties of the graph
				ax.set_title(title)
				ax.set_xlabel('Year')
				ax.set_ylabel('Spending (€)')
				ax.legend(loc='upper left')
				
				print('\n',title,':\n----------')
				print(df_spend)
				plt.tight_layout()
				plt.show()


			## Nº of books over time: group by Date, for all values of Paid, count.
			elif opti==3:
				title = 'Book Acquisitions by Paid category over Time'
				df_acq = df.pivot_table(
					index='Year',
					columns='Paid',
					values='Cost',
					aggfunc='count'
				)
				
				#Create 'others' column
				df_acq['Others'] = df_acq[['Dad','Gift','Grandma','Mom']].sum(axis=1)
				#Delete not used columns
				df_acq = df_acq.drop(['Dad','Gift','Grandma','Mom'], axis=1)
				#Create 'Total' column
				df_acq['Total'] = df_acq.sum(axis=1)
				
				#Plot the columns as bars
				fig, ax = plt.subplots()
				df_acq.plot(
					y=['Myself','Wallet','Others'],
					kind='bar',
					ax=ax,
					color=['blue','red','green'],
					label=['Myself','Wallet','Others']
				)
				#Plot the Total line using the SAME x positions
				ax.plot(
					range(len(df_acq)),
					df_acq['Total'],
					color='black',
					linewidth=2.5,
					zorder=10,
					marker='o',
					label='Total',
				)
				#Other properties of the graph
				ax.set_title(title)
				ax.set_xlabel('Year')
				ax.set_ylabel('Nº of Books')
				ax.legend(loc='upper left')
				
				print('\n',title,':\n----------')
				print(df_acq)
				plt.tight_layout()
				plt.show()


		else:
			print("Option not valid.")

	except ValueError:
		print("Option must be a number")
	
	

