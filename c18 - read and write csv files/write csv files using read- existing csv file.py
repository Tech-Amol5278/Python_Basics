# Writing csv file using existing csv file

from csv import DictReader,DictWriter

# if we want to keep the same header as of existing file
with open('file4.csv') as rf:
    with open('write-dictreader.csv','w',newline='') as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf,fieldnames=['firstname','lastname','age'])
        csv_writer.writeheader()
        for row in csv_reader:
            csv_writer.writerow(row)

# if wa want diffrent headers, try below
with open('file4.csv') as rf:
    with open('write-dictreader_1.csv','w',newline='') as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf,fieldnames=['first_name','last_name','age_'])
        csv_writer.writeheader()
        for row in csv_reader:
            fname,lname,age = row['firstname'],row['lastname'],row['age']
            csv_writer.writerow({
                'first_name':fname.upper(),
                'last_name': lname.upper(),
                'age_':age
            })    
