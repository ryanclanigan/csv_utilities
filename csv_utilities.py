import csv;
import argparse;
import dateutil.parser;
import string
import random
from datetime import datetime
from datetime import timedelta

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
  

parser = argparse.ArgumentParser(description='CSV File Utilities. By default lists all rows in file.')
parser.add_argument('file', metavar='File', help='File to parse or create')
parser.add_argument('-c', '--columns', type=int, nargs='+', help='Selects columns to do work on')
parser.add_argument('-t', '--time', action='store_true', help="""Prints out the time between 
                    the first two columns selected""")
parser.add_argument('-g', '--generate', action='store_true', help="""Generates a csv file with the given filename.
                    Default number of data columns is 1 and default number of rows is 2000.""")
parser.add_argument('--colNum', type=int, help='Number of columns to generate')
parser.add_argument('--rowNum', type=int, help='Number of rows to generate')

args = parser.parse_args()



with open(args.file, 'w+') as csv_file: 
  if args.generate:
    rowNum = 2000 if args.rowNum is None else args.rowNum
    colNum = 1 if args.colNum is None else args.colNum
    headers = ['Time']
    for i in range(0, colNum):
      headers.append(randomString())
    
    writer = csv.writer(csv_file)
    writer.writerow(headers)
    date = datetime.now()
    
    for j in range(0, rowNum):
      values = list()
      values.append(date.isoformat())
      for i in range(0, colNum):
        values.append(str(j))
      writer.writerow(values)
      date = date + timedelta(microseconds=1)
    
  else:
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
      