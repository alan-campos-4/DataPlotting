import sys
import argparse
from datetime import datetime
import pyperclip




if __name__ == "__main__":
	
	parser = argparse.ArgumentParser(
		prog='Date convertor',
		description='...',
		epilog='Text at the bottom for help'
	)
	parser.add_argument("date",				help="date to convert")
	parser.add_argument('-i','--input',		help="format of the input date",		default="%d/%m/%Y")
	parser.add_argument("-o",'--output',	help="new format given to the date",	default="%Y-%m-%d")
	parser.add_argument('--copy',			help="copy the converted date to the clipboard", action="store_true", default=True)
	args = parser.parse_args()
	
	
	try:
		# The date string received converted to a Date object
		date_obj = datetime.strptime(args.date, args.input).date()
		
		# Replace all the elements in the new format with the elements of the date object.
		new_date = args.output.replace("%Y", date_obj.strftime("%Y")).replace("%m", date_obj.strftime("%m")).replace("%d", date_obj.strftime("%d"))
		
		
		# If the option has been selected, copy the date. If not, print it.
		if args.copy:
			pyperclip.copy(new_date)
			print(f' {pyperclip.paste()} copied to clipboard.')
		else:
			print(f'Converted date {new_date}')
		
		
	except KeyboardInterrupt:
		print("\n\nExited program.")
	except Exception as e:
		print("An error occurred:", e)




