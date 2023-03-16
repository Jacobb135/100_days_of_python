import requests
from datetime import date, timedelta


class News:

    def __init__(self):
        self.news_endpoint = "https://newsapi.org/v2/everything"
        self.news_api_key = "API_KEY"
        self.today = date.today()
        self.yesterday = str(self.today - timedelta(days=1))
        self.day_before_yesterday = str(self.today - timedelta(days=2))
        self.news_params = None

    def set_news_params(self, q, sortby):
        self.news_params = {
            "q": q,
            "from": self.yesterday,
            "to": self.yesterday,
            "language": "en",
            "sortBy": sortby,
            "apiKey": self.news_api_key,
        }

    def get_news_articles(self):
        response = requests.get(self.news_endpoint, self.news_params)
        response.raise_for_status()
        data = response.json()
        article = data["articles"][:3]
        headline_list = [headline["title"] for headline in article]
        description_list = [description["description"] for description in article]
        return {"headline_list": headline_list,
                "description_list": description_list}
