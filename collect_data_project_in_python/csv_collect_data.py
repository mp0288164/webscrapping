import csv
# remember file name extention always be ".csv"
file_name='d://mypycsv_collection//movies_name.csv'
row=['manisha','payal','nisha']
# open csv file in write mode
with open(file_name, 'w') as csvfile:  
    # create csvwriter object
    csvwriter=csv.writer(csvfile)
    # write rows in csv file
    csvwriter.writerow(row)