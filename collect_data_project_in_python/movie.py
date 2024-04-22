from bs4  import BeautifulSoup
import subprocess
# import reque
# pandas as pd
import re 
import sys
from datetime import datetime

class MyMovies:
    def __init__(self):
        self.movie_name = []
        self.headers = {'User-Agent':'Mozilla/5.0'}
    def get_movies(self):
        url = 'https://www.imdb.com/chart/top/'
        response = requests.get(url,headers=self.headers)
        soup = BeautifulSoup(response.text,'html.parser')
        movie_row = soup.find('ul',class_='ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 eBRbsI compact-list-view ipc-metadata-list--base')
        for count,row in enumerate(movie_rows.find_all('li'),start=1):
            self.get_data(row)
            print('myname is')
            print(f'processing movie{count}')
        # def get_data_from_each_link(self,li_tag):
        #     self.get_movie_name(self,li_tag)
        # def get_movie_name(self,li_tag):
        #     title=li_tag.find('h3 ').text
        #     movie_name = re.sub(r "^\d+\.\s*',",title)
            # self.movie_name.append(movie_name)
if __name__ == "_main_":
    k=MyMovies()
    k.get_movies()