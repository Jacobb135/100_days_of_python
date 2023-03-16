import smtplib
import datetime as dt
import random

with open("quotes.txt") as quote:
    quotes = quote.readlines()
    random_quote = random.choice(quotes)

now = dt.datetime.now()
day_of_the_week = now.weekday()

my_email = "user@gmail.com"
password = "password"

if day_of_the_week == 1:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="email@gmail.com",
                            msg=f"Subject:Your extra motivational pick me up!\n\n{random_quote}")






