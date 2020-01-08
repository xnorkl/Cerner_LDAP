import argparse
from SPGEN import rename_users

def main():
  parser = argparse.ArgumentParser(
      prog='gen_cerner_usernames',
      description='generate spreadsheet of AD usernames for cerner millennium'
      )
  parser.add_argument(
      '-i',
      dest='rpath',
      help='input path to spreadsheet with list of fullnames'
      )
  parser.add_argument(
      '-o',
      dest='wpath',
      help='output path to spreadsheet'
      )
  parser.add_argument(
      '-disn',
      dest='disn',
      help='specify full name column'
      )
  parser.add_argument(
      '-usrn',
      dest='cernu',
      help='specify cerner username'
      )
  parser.add_argument(
      '-cid',
      dest='cernid',
      help='specify cerner id column'
      )

  args = parser.parse_args()

  columns = [args.disn, args.cernu, args.cernid]
  rename_users(args.rpath, args.wpath, columns)

if __name__ == "__main__":
  main()


