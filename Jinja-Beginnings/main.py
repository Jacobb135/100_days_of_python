from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    random_number = random.randint(1, 10)
    year = datetime.date.today().year
    return render_template('index.html', num=random_number, year=year)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/3e957786b0b24d1eaae5"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


@app.route('/guess/<name>')
def guess(name):
    response = requests.get(f"https://api.agify.io?name={name}")
    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    gender_data = gender_response.json()
    data = response.json()
    age = data["age"]
    gender = gender_data["gender"]
    return render_template("guess.html", name=name, gender=gender, age=age)

if __name__ == '__main__':
    app.run(debug=True)
