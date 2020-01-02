### AD Cerner Map ###

import csv
from getpass import getpass
import ldap
import pprint

## Pretty Print ##
pp = pprint.PrettyPrinter(indent=1)

## Prompt ##
#user = input('Username: ')
user = 'gordont@monhealthsys.org'
pssw = getpass()

## LDAP INIT ##
conn = ldap.initialize('ldap://172.26.5.141')
conn.protocol_version = 3
conn.set_option(ldap.OPT_REFERRALS, 0)
conn.simple_bind_s(user,pssw)

## Search ##
response = conn.search_s(
    'dc=mhs,dc=org', ldap.SCOPE_SUBTREE,
    'userPrincipalName=abbasz@monhealthsys.org')
pp.pprint(response)



