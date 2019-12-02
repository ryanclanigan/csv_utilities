import csv;
import dateutil.parser;
import argparse;


parser = argparse.ArgumentParser(description='CSV File Utilities. By default lists all rows in file.')
parser.add_argument('file', metavar='F', help='File to parse')
parser.add_argument('-c', '--columns', type=int, nargs='+', help='Selects columns to do work on')
parser.add_argument('-t', '--time', action='store_true', help="""Prints out the time between 
                    the first two columns selected""")


args = parser.parse_args()

with open(args.file) as csv_file: 
  csv_reader = csv.reader(csv_file)
  for row in csv_reader: 
    if args.time:  
      beforetime = dateutil.parser.parse(row[args.columns[0]])
      aftertime = dateutil.parser.parse(row[args.columns[1]])

      diff = aftertime - beforetime
      total_seconds = diff.total_seconds()
      print(total_seconds)
    
    else: 
      print(row)
      