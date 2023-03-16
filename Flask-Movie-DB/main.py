from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy()
db.init_app(app)


class MovieForm(FlaskForm):
    movie_rating = FloatField('Rating out of 10 e.g 6.9', validators=[DataRequired()])
    movie_review = StringField('Your review', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddForm(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), unique=True)
    year = db.Column(db.Integer)
    description = db.Column(db.String(250))
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250))

    def __repr__(self):
        return f"<Movie {self.title}>"


# with app.app_context():
#     db.create_all()
#     new_movie = Movie(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favourite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#     )
#     db.session.add(new_movie)
#     db.session.commit()


@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating).all()

    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
    db.session.commit()
    return render_template("index.html", all_movies=movies)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = MovieForm()
    movie_id = request.args.get('index')
    movie_to_change = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie_to_change.rating = form.movie_rating.data
        movie_to_change.review = form.movie_review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie_to_change, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get('index')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=['GET', 'POST'])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        movie_to_search = add_form.movie_title.data
        response = requests.get(
            f"https://api.themoviedb.org/3/search/movie?api_key=7161afdd2a8c4686c8e7f43cd82ab94e&language=en-US&query={movie_to_search}&page=1&include_adult=false").json()
        data = response["results"]
        return render_template('select.html', movies=data)
    return render_template('add.html', form=add_form)


@app.route("/select")
def select():
    movie_id = request.args.get('index')
    data = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=7161afdd2a8c4686c8e7f43cd82ab94e&language=en-US").json()
    movie_to_add = Movie(
        title=data['title'],
        year=data['release_date'],
        description=data['overview'],
        rating=None,
        ranking=None,
        review=None,
        img_url=f"https://image.tmdb.org/t/p/original{data['poster_path']}"
    )
    db.session.add(movie_to_add)
    db.session.commit()
    return redirect(url_for('edit', index=movie_to_add.id))


if __name__ == '__main__':
    app.run(debug=True)
