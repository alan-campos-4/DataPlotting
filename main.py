import argparse
from albums import album_analysis
from books import book_analysis


#Action to list all the available datatables
class _ListAction(argparse.Action):
	def __init__(self, option_strings, dest=argparse.SUPPRESS, default=argparse.SUPPRESS, help=None):
		super(_ListAction, self).__init__(option_strings=option_strings, dest=dest, default=default, nargs=0, help=help)
	def __call__(self, parser, namespace, values, option_string=None):
		print("Available datatables:")
		for dt in datatables:
			print(" - ",dt)
		parser.exit()




datatables = ["Albums", "Books"]


if __name__ == "__main__":
	
	parser = argparse.ArgumentParser(
		prog='Basic data analysis',
		description='This program uses datatables for data analysis and graph plotting.',
		epilog='Text at the bottom for help'
	)
	parser.add_argument("dt_name", choices=datatables, help="name of the datatable to analyse")
	exc_gr = parser.add_mutually_exclusive_group()
	exc_gr.add_argument("-v","--view",	 help="view the datatable or perform data analysis", action="store_true", default=True)
	exc_gr.add_argument("-u","--update", help="add or modify data of the datatable",         action="store_true")
	parser.add_argument('--graph',       help="show the graph corresponding to the table",   action=argparse.BooleanOptionalAction, default=True)
	parser.add_argument('-l', '--list',  help="list all available datatables",               action=_ListAction)
	args = parser.parse_args()
	
	if args.update:
		args.view = False
	
	try:
		if args.dt_name=="Albums":
			album_analysis(args.view, args.update, args.graph)
		elif args.dt_name=="Books":
			book_analysis(args.view, args.update, args.graph)
		
	except KeyboardInterrupt:
		print("\n\nExited program.")



