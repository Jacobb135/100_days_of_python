from stock import StockPrice
from news import News
from send_sms import Sms

stock = StockPrice()
news = News()
sms = Sms()

stock.set_stock_params("DIGITAL_CURRENCY_DAILY", "BTC", "USD")
percentage = stock.get_stock_percentage()["percentage"]
yesterday_close = stock.get_stock_percentage()["yesterday_close"]
day_before_yesterday_close = stock.get_stock_percentage()["day_before_yesterday_close"]

if percentage > 5:
    news.set_news_params("q", "popularity")
    news.get_news_articles()
    news_list = news.get_news_articles()
    headline_list = news_list["headline_list"]
    description_list = news_list["description_list"]
    if yesterday_close > day_before_yesterday_close:
        ticker = "🔺"
    else:
        ticker = "🔻"

    sms.send_sms(ticker, percentage, headline_list, description_list)

