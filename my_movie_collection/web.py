from bs4 import BeautifulSoup
import requests
html_text = requests.get("https://www.indianyellowpages.com/neemuch/").text
soup = BeautifulSoup(html_text,'html.parser')
movie_details = soup.find('div',class_="container")
# print(movie_details)
movie_name = movie_details.find('div', class_="rj_ser_det")
print(movie_name)
# for movie in movie_details:
#    movie_name=movie_details.find('a',class_="ipc-title-link-wrapper").text
#    print(movie_name)
