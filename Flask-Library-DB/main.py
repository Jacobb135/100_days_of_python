from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()

db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"


with app.app_context():
    db.create_all()
    db.session.commit()


@app.route('/')
def home():
    books = db.session.query(Book).all()
    return render_template('index.html', all_books=books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title'].title()
        author = request.form['author'].title()
        rating = request.form['rating'].title()
        new_book = Book(title=title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit", methods=['POST', 'GET'])
def edit():
    if request.method == 'POST':
        book_id = request.form['id']
        new_rating = request.form['new_rating']
        book_to_update = Book.query.filter(Book.id == book_id).first()
        book_to_update.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))

    book_id = request.args.get('id')
    book_selected = Book.query.filter(Book.id == book_id).first()
    return render_template("edit.html", book=book_selected)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

