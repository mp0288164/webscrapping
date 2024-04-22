from bs4 import BeautifulSoup
import requests,csv
source = requests.get('http://www.imdb.com/chart/top')
soup = BeautifulSoup(source.text, 'html.parser')

    
movies = soup.find('tbody', class_="lister-list").find_all('tr')
    
for movie in movies: 
    name = movie.find('td',class_="titleColumn").a.text
    rank = movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]
    year = movie.find('td',class_="titleColumn").span.text.strip('()')
    rating = movie.find('td',class_="ratingColumn imdbRating").strong.text
    
    print(rank,name,year,rating)

import files 
data.to_csv('sample.csv') 
files.download("sample.csv")
