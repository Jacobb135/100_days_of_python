from flask import Flask, render_template, request
import requests
import smtplib


EMAIL_ADDRESS = "user@gmail.com"
PASSWORD = "email_password_key"
data = requests.get("https://api.npoint.io/b1456133ea498bc53422").json()


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", data=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html")
    else:
        name = request.form['name']
        email = request.form['email']
        number = request.form['number']
        message = request.form['message']
        send_email(name, email, number, message)
        return render_template('contact.html')


def send_email(name, email, number, message):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(user=EMAIL_ADDRESS, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL_ADDRESS,
                            to_addrs="email@gmail.com",
                            msg=f"{name}\n"
                                f"{email}\n"
                                f"{number}\n"
                                f"{message}")


@app.route("/post/<int:index>")
def get_post(index):
    for post in data:
        if post["id"] == index:
            requested_post = post
    return render_template("post.html", index=requested_post)


if __name__ == '__main__':
    app.run(debug=True)
