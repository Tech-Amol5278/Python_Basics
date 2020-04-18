
# Writing csv files
    # writer
        # writerow - to append one row at a a time
        # writerows - to append multiple rows at a time

from csv import writer ## Importing writer class from csv module


with open('file3.csv','w',newline='') as f:  ## newline='' to remove the blank lines
    csv_writer = writer(f)
    ## using writerow
    csv_writer.writerow(['name','country'])
    csv_writer.writerow(['amol','India'])
    csv_writer.writerow(['akshay','Nepal'])
    ## using writerows
    csv_writer.writerows([['umesh','germany'],['ashish','london'],['sagar','france']])






