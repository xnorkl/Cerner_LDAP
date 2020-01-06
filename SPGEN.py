### SPREAD SHEET GENERATOR ###

from openpyxl import Workbook
from UNGEN import list_usernames
import random
import string

## Configs ##
rpath = 'Providers.xlsx'
wpath = 'Test.xlsx'
pwlen = 8

## Worksheet Configs ##
wb = Workbook()
mill = wb.create_sheet("millenium users", 0)
lost = wb.create_sheet("users not in ad", 1)

# list_usernames takes a file path and a column to parse
# returns a list of millienium usernames that match existing AD SAM account names
# and a list of usernames that do not exist in AD, but do in millenium
mill_users, lost_users = list_usernames(rpath,'B')

mill.append(['Username','Password'])
lost.append(['Username'])

cred = []

def create_pw(n: int) -> str:
  pw = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(n))
  return pw

for uname in mill_users:
  cred = [uname, create_pw(pwlen)]
  mill.append(cred)

for uname in lost_users:
  uname = [uname]
  lost.append(uname)

wb.save(wpath)


