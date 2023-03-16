import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movie_webpage = response.text
soup = BeautifulSoup(movie_webpage, 'html.parser')

movie_title = soup.find_all("h3")

movie_list = []
with open("movies.txt", "w", encoding='utf8') as file:
    for title in reversed(movie_title):
        movie_list.append(f"{title.text}\n")
    file.writelines(movie_list)



