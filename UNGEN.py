### AD USERNAME GENERATOR ###

from getpass import getpass, getuser
import ldap
from PARSR import split_list
from socket import gethostname
from typing import List

## Configs ##

## Prompt ##
user = input('Username: ')
uprn = user + '@mydomain.org'
pssw = getpass()

## LDAP Configs ##
conn = ldap.initialize('ldap://0.0.0.0')
conn.protocol_version = 3
conn.set_option(ldap.OPT_REFERRALS, 0)
conn.simple_bind_s(uprn,pssw)

## Create Millenium Usernames ##

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

def list_usernames(full_names: List[str], col: str) -> List[str]:
  split_names = [name for name in split_list(full_names) if name]
  lost_users = []
  mill_users = [create_username(name, lost_users) for name in split_names]

  return mill_users, lost_users


