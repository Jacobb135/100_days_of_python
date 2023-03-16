from flask import Flask, render_template
import requests


app = Flask(__name__)
response = requests.get("https://api.npoint.io/07fd00f5e7009251e266")
data = response.json()


@app.route('/')
def home():
    return render_template("index.html", all_posts=data)


@app.route("/blog/<int:index>")
def get_blog(index):
    for blog_post in data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
