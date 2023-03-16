import requests

movie = "the matrix"
data = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key=7161afdd2a8c4686c8e7f43cd82ab94e&language=en-US&query={movie}&page=1&include_adult=false").json()
print(data["results"][0])
# print(data["results"]["release_date"])