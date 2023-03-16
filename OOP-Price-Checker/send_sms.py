from twilio.rest import Client

class Sms:

    def __init__(self):
        self.account_sid = "ACCOUNT_SID"
        self.auth_token = "AUTH_TOKEN"
        self.twilio_number = "+TWILIO_NUMBER"
        self.to_number = "+MY_NUMBER"

    def send_sms(self, ticker, percentage, headline_list, description_list):
        count = 0
        while count < 3:
            client = Client(self.account_sid, self.auth_token)
            message = client.messages \
                .create(
                    body=f"BTC: {ticker} {percentage}%\n"
                         f"Headline: {headline_list[count]}\n"
                         f"Brief: {description_list[count]}\n",
                    from_="+18557853365",
                    to="+18124496487"
            )
            count += 1
