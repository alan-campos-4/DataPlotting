import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime




books = pd.read_csv('datasheets/spending_books.csv', on_bad_lines='warn')
df_books = pd.DataFrame(books)	#shape = (233,10)
#pd.set_option('display.max_rows', 233)


def book_analysis():
	df1 = 	df_books

	#Change the datatype of the Date column
	df1['Date'] = pd.to_datetime(df1['Date'])
	#Add the the Year column for sorting
	df1['Year'] = df1['Date'].dt.year
	#Replace NaNs with 0
	df1.fillna(0, inplace=True)


	## Books spending over time: group by Date, for all values of Paid, show cost. Complete - others
	print('\nBook Spending by Paid category over Time: \n----------')
	df_spend = df1.pivot_table(
		index='Year',
		columns='Paid',
		values='Cost',
		aggfunc='sum'
	)
	#Add 'others' column

	#Add total column

	#Add total row
	df_spend.loc['Total'] = df_spend.sum()
	print(df_spend)


	"""
	## Nº of books over time: group by Date, for all values of Paid, count. Complete - others
	print('\nNº of Books Acquired by Paid category over Time: \n----------')
	df_acq = df1.pivot_table(
		index='Year',
		columns='Paid',
		values='Cost',
		aggfunc='count'
	)
	print(df_acq)
	"""



