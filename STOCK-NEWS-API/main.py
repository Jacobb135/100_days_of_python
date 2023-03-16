import requests
from datetime import date, timedelta
from twilio.rest import Client

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "API_KEY"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "API_KEY"
ACCOUNT_SID = "ACCOUNT_SID"
AUTH_TOKEN = "AUTH_TOKEN"
TWILIO_NUMBER = "+TWILIO_NUMBER"

today = date.today()
yesterday = str(today - timedelta(days=1))
day_before_yesterday = str(today - timedelta(days=2))


stock_params = {
    "function": "DIGITAL_CURRENCY_DAILY",
    "symbol": "BTC",
    "market": "USD",
    "apikey": STOCK_API_KEY
}

news_params = {
    "q": "BTC",
    "from": yesterday,
    "to": yesterday,
    "language": "en",
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY,
}


response = requests.get(STOCK_ENDPOINT, stock_params)
response.raise_for_status()
data = response.json()
yesterday_close = float(data["Time Series (Digital Currency Daily)"][yesterday]["4a. close (USD)"])
day_before_yesterday_close = float(data["Time Series (Digital Currency Daily)"][day_before_yesterday]["4a. close (USD)"])
price_difference = abs(yesterday_close - day_before_yesterday_close)
average = (yesterday_close + day_before_yesterday_close) / 2
percentage = 6

if percentage > 5:
    response = requests.get(NEWS_ENDPOINT, news_params)
    response.raise_for_status()
    data = response.json()
    article = data["articles"][:3]

    headline_list = [headline["title"] for headline in article]
    description_list = [description["description"] for description in article]
    url_list = [url["url"] for url in article]

    if yesterday_close > day_before_yesterday_close:
        ticker = "🔺"
    else:
        ticker = "🔻"
    count = 0
    # for _ in range(3):
    #     client = Client(ACCOUNT_SID, AUTH_TOKEN)
    #     message = client.messages \
    #         .create(
    #             body=f"BTC: {ticker} {percentage}% Headline: {headline_list[count]}\nBrief: {description_list[count]}\n{url_list[count]}",
    #             from_=TWILIO_NUMBER,
    #             to="+18124496487"
    #     )
    #     count += 1

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
            .create(
                body="It's going to rain today. Remember to bring an umbrella!",
                from_="+TWILIO_NUMBER",
                to="+YOUR_PHONE_NUMBER",
    )
    print(message.status)
