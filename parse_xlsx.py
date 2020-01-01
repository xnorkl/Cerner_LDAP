## Parse XLSX ##

from openpyxl import load_workbook
import pprint


path = 'Providers.xlsx'
wb = load_workbook(path)
ws = wb.active
Name = ws['B']
Name_list = [Name[x].value for x in range (len(Name))]
pp = pprint.PrettyPrinter(indent=1)
pp.pprint(Name_list)
## TODO ##
# FIRST: Make REGEX to Parse Names into a list of 3-tuple NAMES(First,Last,Middle)
# THEN: Outline the functions needed to parse the data from the given xlsx files
#       so that the final output is a dictionary USERNAMES{'IN_AD','NOT_IN_AD'}  
