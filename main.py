import argparse
from albums import album_analysis
from books import book_analysis



if __name__ == "__main__":
	parser = argparse.ArgumentParser(
		prog='Basic data analysis',
		description='This program uses datatables for data analysis and graph plotting.',
		epilog='Text at the bottom for help'
	)
	parser.add_argument("title", help="Datatable to analyse")
	parser.add_argument('--graph', default=True, action=argparse.BooleanOptionalAction, help="show the graph corresponding to the table")
	#parser.add_argument('-v','--view', action=bool, help="show the content of the table")
	#parser.add_argument('-u','--update', type=bool, help="update the content of the table")
	args = parser.parse_args()
	
	
	print(args.view)
	
	if args.title=="Albums":
		album_analysis()
	elif args.title=="Books":
		book_analysis()
	else:
		print("Argument not valid")


