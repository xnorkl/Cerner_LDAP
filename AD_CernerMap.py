### AD Cerner Map ###

from getpass import getpass
import ldap
import pprint
from PARSER import list_column, split_list
from typing import List

## Configs ##

# Pretty Print #
pp = pprint.PrettyPrinter(indent=1)

# SpreadSheet #
path = 'Providers.xlsx'

## Prompt ##
user = 'gordont@monhealthsys.org'
pssw = getpass()

## LDAP Configs ##
conn = ldap.initialize('ldap://172.26.5.141')
conn.protocol_version = 3
conn.set_option(ldap.OPT_REFERRALS, 0)
conn.simple_bind_s(user,pssw)

## Create Usernames ## 
## Query User ##
## TODO ##
# 
# 
def check_username(uname: str) -> bool:
  sam = 'sAMAccountName=' + uname
  response = conn.search_s('dc=mhs,dc=org', ldap.SCOPE_SUBTREE, sam)
  answer = str([tuple[0] for tuple in response][0])
  # If answer is None return False
  if answer == 'None':
    return False
  return True

def create_username(name: List[str], lost: List[str]) -> str:
  rubric    = ['Last','First','Mid']
  named = {k:v for k,v in zip(rubric,name)}
  if len(named['First']) == 1:
    pocket = named['First']
    named['First'] = named['Mid']
    named['Mid'] = pocket
  username  = named['Last'] + named['First'][0]
  # If username does not exist
  if not check_username(username):
     lost.append(username)
  return username

def list_usernames(path: str, col: str) -> List[str]:
  full_names = list_column(path,col)
  names = [name for name in split_list(full_names) if name]
  lost_users = []
  mill_users = [create_username(name, lost_users) for name in names]
  #users = [list(filter(None,users)) for name in users]
  return mill_users, lost_users

mill_users, lost_users = list_usernames(path,'B')
pp.pprint(mill_users)
pp.pprint(lost_users)
