import csv
import requests

response = requests.get("https://m.imdb.com/chart/top/")
filename='mycsvmovie.csv'
cr=csv.reader(response)
with open('filename','w') as csvfile:
    
    