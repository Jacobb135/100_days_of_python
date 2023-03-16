from bs4 import BeautifulSoup
import requests
import smtplib



ACCEPT = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
AMAZON_LINK = "https://www.amazon.com/ZOTAC-Graphics-IceStorm-Advanced-ZT-A30900J-10P/dp/B08ZL6XD9H/ref=sr_1_3?crid=236HU95FS8KRJ&keywords=rtx+3090&qid=1676332669&sprefix=rtx+3090%2Caps%2C120&sr=8-3"

headers = {
    "Accept-Language": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
}


response = requests.get(AMAZON_LINK, headers=headers)
webpage = response.text
soup = BeautifulSoup(webpage, "lxml")
# price = int(soup.select(".a-price-whole")[0].getText().split(".")[0])
price = 999
if price < 1000:

    my_email = "email@gmail.com"
    password = "password_key"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="email@gmail.com",
                            msg=f"Subject: It's your lucky day\n\nThe price of your 3090 is now affordable :)")