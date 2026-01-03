import argparse
from albums import album_analysis
from books import book_analysis



if __name__ == "__main__":
	parser = argparse.ArgumentParser(
		prog='Basic data analysis',
		description='This program uses datatables for data analysis and graph plotting.',
		epilog='Text at the bottom for help'
		)
	parser.add_argument("title", help="Subject to apply analysis to")
	args = parser.parse_args()
	
	
	if args.title=="Albums":
		album_analysis()
	elif args.title=="Books":
		book_analysis()
	else:
		print("Argument not valid")



