import requests
from datetime import date, timedelta


class StockPrice:
    def __init__(self):
        self.stock_endpoint = "https://www.alphavantage.co/query"
        self.stock_api_key = "API_KEY"
        self.today = date.today()
        self.yesterday = str(self.today - timedelta(days=1))
        self.day_before_yesterday = str(self.today - timedelta(days=2))

    def set_stock_params(self, function, symbol, market):
        self.stock_params = {
            "function": function,
            "symbol": symbol,
            "market": market,
            "apikey": self.stock_api_key
        }

    def get_stock_percentage(self):
        response = requests.get(self.stock_endpoint, self.stock_params)
        response.raise_for_status()
        data = response.json()
        yesterday_close = float(data["Time Series (Digital Currency Daily)"][self.yesterday]["4a. close (USD)"])
        day_before_yesterday_close = float(data["Time Series (Digital Currency Daily)"][self.day_before_yesterday]["4a. close (USD)"])
        price_difference = abs(yesterday_close - day_before_yesterday_close)
        average = (yesterday_close + day_before_yesterday_close) / 2
        percentage = price_difference / average * 100
        return {"yesterday_close": yesterday_close,
                "day_before_yesterday_close": day_before_yesterday_close,
                "percentage": percentage}


