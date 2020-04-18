## Read csv files

from csv import DictReader      ## Importing dictreader class from csv module

with open('test1.csv','r') as f:
    csv_reader = DictReader(f)
    for row in csv_reader:
        print(row)
        print(row['name'])
        print(row['email'])

## Default delimiter for csv is comma(,) but to read csv files which has diffrent delimiter, see below

with open('test_pipe.csv','r') as f:
    csv_reader = DictReader(f,delimiter='|')
    for row in csv_reader:
        print(row)
        print(row['name'])
        print(row['email'])





