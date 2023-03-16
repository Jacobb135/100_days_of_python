from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, url
import csv

"https://www.google.com/search?client=firefox-b-1-d&tbs=lf:1,lf_ui:4&tbm=lcl&sxsrf=AJOqlzViuI0g0pohslTntLd-plEKglZuXQ:1678116767772&q=loyal+coffee&rflfq=1&num=10&ved=2ahUKEwi6ptaO0Mf9AhW3ADQIHdWxD1QQtgN6BAgUEAE#rlfi=hd:;si:8246076144351921910;mv:[[39.012982199999996,-104.7982097],[38.8172916,-104.82377799999999]]"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps', validators=[DataRequired(), url()])
    open = StringField('Opening time e.g.', validators=[DataRequired()])
    closing_time = StringField('Closing time e.g. 11PM', validators=[DataRequired()])
    coffee_rating = SelectField(u'Coffee Rating', choices=["☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️",
                                                           "☕️☕️☕️☕️☕️"], validators=[DataRequired()])
    wifi_rating = SelectField(u'Wifi Strength Rating', choices=["✘", "💪", "💪💪", "💪💪💪",
                                                    "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_rating = SelectField(u'Power Socket Availability', choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌",
                                                    "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', encoding='utf8') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.closing_time.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.power_rating.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
