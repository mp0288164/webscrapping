import csv
import requests


def fetch_data_from_link(link):
    response = requests.get(link)

    if response.status_code == 200:
        return response.text
    else:
        print('faild to fetch from link')
        return None



if __name__ =="__main__":
    link ="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=MSFT&apikey=demo&datatype=csv"
    filename="d://mypycsv_collection//movies_list.csv"

data= fetch_data_from_link(link)

def save_as_csv(data,filename):
    rows = data.split('\n')
    with open(filename, 'w') as csvfile:
        #create csvwriter object
        csvwriter = csv.writer(csvfile)

    # for row in rows():
        # csvwriter.writerow(row.split(','))

    for line in response.iter_lines():
        csvwriter.writerow(line.decode('utf-8').split(','))
    
if data:
    save_as_csv(data,filename)
    print("data save successfully")