import argparse

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
    '-fn',
    dest='fulln',
    help='specify full name column'
    )
parser.add_argument(
    '-id',
    dest='cernid'
    help='specify cerner id column'
    )


