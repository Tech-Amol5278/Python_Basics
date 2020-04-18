
# Writing csv files
    # dictwriter
        # writerow - to append one row at a a time
        # writerows - to append multiple rows at a time

from csv import DictWriter ## Importing DictWriter class from csv module


with open('file4.csv','w',newline='') as f:  ## newline='' to remove the blank lines
   csv_writer = DictWriter(f,fieldnames=['firstname','lastname','age'])
   csv_writer.writeheader()   ## for writing only headers
   # writing rows using write writerow
   csv_writer.writerow({'firstname':'Amol','age':'30','lastname':'chavan'})
   csv_writer.writerow({'firstname':'umesh','lastname':'patil','age':'31'})
   # writing rows using write writerows
   csv_writer.writerows([
        {'firstname':'Niraj','age':'26','lastname':'Salokhe'},
        {'firstname':'Vikrant','age':'27','lastname':'Hande'}
   ])
