import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")
    

@app.route("/random")
def get_random_cafe():
    cafes = Cafe.query.all()
    random_cafe = random.choice(cafes)
    return jsonify(id=random_cafe.id,
                   name=random_cafe.name,
                   map_link=random_cafe.map_url,
                   img_url=random_cafe.img_url,
                   location=random_cafe.location,
                   seats=random_cafe.seats,
                   has_toilet=random_cafe.has_toilet,
                   has_wifi=random_cafe.has_wifi,
                   has_sockets=random_cafe.has_sockets,
                   can_take_calls=random_cafe.can_take_calls,
                   coffee_price=random_cafe.coffee_price)



## HTTP GET - Read Record
@app.route("/all")
def all_cafes():
    all_cafes = Cafe.query.all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search")
def search():
    cafe_search = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=cafe_search).first()
    if cafe:
        return jsonify(cafes=[cafe.to_dict()])
    else:
        return jsonify(error={
            "Not Found": "We don't have a cafe at that location"
        })
## HTTP POST - Create Record
@app.route("/add", methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
                   name=request.form.get('name'),
                   map_url=request.form.get('map_url'),
                   img_url=request.form.get('img_url'),
                   location=request.form.get('location'),
                   seats=request.form.get('seats'),
                   has_toilet=bool(request.form.get('has_toilet')),
                   has_wifi=bool(request.form.get('has_wifi')),
                   has_sockets=bool(request.form.get('has_sockets')),
                   can_take_calls=bool(request.form.get('can_take_calls')),
                   coffee_price=request.form.get('coffee_price'))
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added cafe."})


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe_to_update = db.session.query(Cafe).filter_by(id=cafe_id).first()
    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        return jsonify({"success": "Successfully updated the price"})
    else:
        return jsonify(error={"Not found": "Sorry there is no cafe with that id"}), 404
## HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=['DELETE'])
def report_closed(cafe_id):
    cafe_to_close = db.session.query(Cafe).filter_by(id=cafe_id).first()
    if cafe_to_close:
        api_key = request.args.get("api_key")
        if api_key == "TopSecretAPIKey":
            db.session.delete(cafe_to_close)
            return jsonify({"success": "Cafe has been deleted"})
        else:
            return jsonify({"error": "Sorry that's not allowed. Make sure you have the right api_key"})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found"}), 404
if __name__ == '__main__':
    app.run(debug=True)
