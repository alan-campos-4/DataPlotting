import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


"""
EXCEL		PANDAS
Worksheet	Dataframe
Column		Series
Row heading	Index
Row			Row
Emptycell	NaN
"""


books = pd.read_csv('Spending_books.csv', on_bad_lines='warn')
df_books = pd.DataFrame(books)	#shape = (233,10)

#pd.set_option('display.max_rows', 233)




#Change the datatype of the Date column
df_books['Date'] = pd.to_datetime(df_books['Date'])
#Add the the Year column
df_books['Year'] = df_books['Date'].dt.year


## Books spending over time: group by Date, for all values of Paid, show cost
print('\nBook Spending over Time: \n----------') 
print(df_books.pivot_table(
	index='Year',
	columns='Paid',
	values='Cost',
	aggfunc='sum'
))


"""
## Nº of books over time: group by Date, for all values of Paid, count
print('\nNº of Books over Time: \n----------')
print(df_books.pivot_table(
	index='Date',
	columns='Paid', 
	values='Cost',
	aggfunc='count'))
"""



