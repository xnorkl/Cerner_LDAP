### XLSX PARSER ###

from bisect import insort
from openpyxl import load_workbook
from typing import List, Dict, Iterable
import re

def list_column(spreadsheet: str, column: str) -> List[str]:
  ## Takes a path to an xlsx and a column and returns a list
  wb = load_workbook(spreadsheet)
  worksheet = wb.active
  return worksheet[column]

def normalize_list(names: List[str]) -> List[str]:
  ## Takes a List of full names and normalizes list ##
  # Tokens to remove absolutely
  clean = str.maketrans(dict.fromkeys("(),_."))

  # Remove any Names containing Test
  # Remove any (<WORD>)
  # [A-Z]{2,}    : Remove any caps words of two or more chars (i.e., MD,PHD,etc)
  # \b[A-Z]?-\S+ : Remove '-' and any following word
  # (\s)(?=\s)   : Remove double whitespaces
  normalized: List[str] = [re.sub(
    r'(Test\s.*)|(Cerner)|(Physician)|(Advisor)|(\sHw)|(De La)|(O\')|(^St\s)|[A-Z]{2,}|\b[A-Z]?-\S+|(\s)(?=\s)',
    '',
    str(n.value).translate(clean)
    ).strip() for n in names]
  return normalized

def split_list(names: List[str]) -> List[List[str]]:
  # Takes a list of names and returns a list of each name in a full name
  # If no middle name is given, create a NULL value
  normal = normalize_list(names[1:])
  split_names = list(
      sub.append('NULL') or sub if len(sub) == 2
      else sub
      for sub in list(re.split(r'\s', name) for name in normal))

  # Filter out blank elements
  split_names = [list(filter(None,name)) for name in split_names]
  return split_names

def stringify(m_list: List[str]) -> List[str]:
  str_list: List[str] = [re.sub(
    r'(ANESTHEV)|(CACTR\S+)|(FBCMD)|(OBNP)|(OBPA)|(None)',
    '',
    str(e.value)).strip() for e in m_list[1:]]

  return list(filter(None,str_list))


