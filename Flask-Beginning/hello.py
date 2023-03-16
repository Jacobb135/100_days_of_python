from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<strong>" + function() + "</strong>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

def make_emphasize(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, world!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media0.giphy.com/media/12ELmx0C4EFKcE/giphy.gif?cid=ecf05e47qh98mmbob02n600eu1y0h9t6yh0ecieolee3isq1&rid=giphy.gif&ct=g" width=200>'



@app.route("/bye")
@make_underlined
@make_bold
@make_emphasize
def bye():
    return "Bye!"


@app.route("/username/<name>/int:number")
def greet(name, number):
    return f"Hello there {name}! You are {number} years old"


if __name__ == "__main__":
    app.run(debug=True)
