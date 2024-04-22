# import csv
# import requests

# # url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=MSFT&apikey=demo&datatype=csv'
# url = 'https://m.imdb.com/chart/top/'
# response = requests.get(url)        

# with open('out.csv', 'w') as f:
#     writer = csv.writer(f)
#     for line in response.iter_lines():
#         writer.writerow(line.decode('utf-8').split(','))
import urllib.request

csv_url = ''

urllib.request.urlretrieve(csv_url, 'MSFT.csv')