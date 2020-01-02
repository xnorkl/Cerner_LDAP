## Parse XLSX ##
from bisect import insort
from openpyxl import load_workbook
from os import path
from typing import List, Dict, Iterable
import re
import pprint 

# Set PPrint
pp = pprint.PrettyPrinter(indent=1)

# Set workbook (path can be improved)
path = 'Providers.xlsx'

def list_column(spreadsheet: str, column: str) -> List[str]:
  ## Takes a path to an xlsx and a column and returns a list 
  ## TODO ##
  # Path should be more than a str, meaning check OS and then use appropriate
  # function to check if path exists
  wb = load_workbook(spreadsheet)
  worksheet = wb.active
  # Full Name column of Workbook
  return worksheet[column]

def normalize_list(names: List[str]) -> List[str]:
  ## Takes a List of full names and normalizes list ##
  # Tokens to remove absolutely
  de_s  = "(),_."
  clean = str.maketrans(dict.fromkeys(de_s))

  # Remove tokens that can't be removed absolutely 
  normalized: List[str] = sorted([re.sub(
    r'(Test\s.*)|(Cerner)|(Physician)|(Advisor)|(\sHw)|(De La)|(^St\s)|[A-Z]{2,}|\b[A-Z]?-\S+|(\s)(?=\s)',
    # Remove any Names containing Test
    # Remove any (<WORD>)
    # [A-Z]{2,}     : Remove any al caps words of two or more chars (i.e., MD,PHD,etc)
    # \b[A-Z]?-\S+  : Remove '-' and any following word
    # (\s)(?=\s)    : Remove double whitespaces 
    '',
    str(n.value).translate(clean)).strip()
    for n in names
    ])
  return normalized

def split_list(names: List[str]) -> List[List[str]]:
  # Takes a list of names and returns a list of each name in a full name
  # If no middle name is given, create a NULL value
  normal = normalize_list(names[1:])
  
  split_names = list(
      sub.append('NULL') or sub if len(sub) == 2 
      else sub 
      for sub in list(re.split(r'\s', name) for name in normal))
  
  split_names = [list(filter(None,name)) for name in split_names]
  return split_names

def create_username(name: List[str]) -> str:
  rubric    = ['Last','First','Mid']
  user_dict = {k:v for k,v in zip(rubric,name)}
  if not len(user_dict['First']) > 1:
    pocket = user_dict['First']
    user_dict['First'] = user_dict['Mid']
    user_dict['Mid'] = pocket 
  username  = user_dict['Last']+user_dict['First'][0]
  return username

def list_usernames(path: str, col: str) -> List[str]:
  full_names = list_column(path,col)
  names = [n for n in split_list(full_names) if n]
  users = []
  for name in names:
    users.append(create_username(name))
  return users

answer = list_usernames(path,'B')
print(len(answer))
