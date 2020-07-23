import os
from os import path
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

if path.exists('env.py'):
    import env

app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')


mongo = PyMongo(app)


# Home Page
@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")


@app.route('/get_drink')
def get_drink():
    """
    Get Drinks: View all drinks in database with the option to filter
    """
    return render_template('drinks.html', boba=mongo.db.boba.find())


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Search Drinks function. Uses regular expressions
    """
    query = request.form.get("query")
    boba = list(mongo.db.boba.find({"drink_type":
                {"$regex": query, "$options": "i"}}))
    return render_template("drinks.html", boba=boba)


@app.route('/see_one/<boba_id>')
def see_one(boba_id):
    """
    Page to view one drink from the database
    """
    boba = mongo.db.boba.find_one({"_id": ObjectId(boba_id)})
    return render_template('components/drinkCard.html', boba=boba)


@app.route("/add_drink")
def add_drink():
    """
    Add Drink form
    """
    drinks = mongo.db.drinks.find()
    teas = mongo.db.teas.find()
    toppings = mongo.db.toppings.find()
    sweet = mongo.db.sweet.find()
    ice = mongo.db.ice.find()
    return render_template('addDrink.html',
                           boba=mongo.db.boba.find(),
                           drinks=list(drinks),
                           teas=teas,
                           toppings=toppings,
                           sweet=sweet,
                           ice=ice)


@app.route('/insert_drink', methods=['POST'])
def insert_drink():
    """
    Function to post user data to the database
    """
    boba = mongo.db.boba
    boba.insert_one(request.form.to_dict())
    return redirect(url_for('get_drink'))


@app.route('/edit_drink/<boba_id>')
def edit_drink(boba_id):
    """
    Edit Drink Form
    """
    boba = mongo.db.boba.find_one({"_id": ObjectId(boba_id)})
    drinks = list(mongo.db.drinks.find())
    teas = list(mongo.db.teas.find())
    top = list(mongo.db.toppings.find())
    decaf = list(mongo.db.decaf.find())
    ice = list(mongo.db.ice.find())
    sweet = list(mongo.db.sweet.find())
    return render_template('components/editDrink.html',
                           boba=boba,
                           drinks=drinks,
                           teas=teas,
                           top=top,
                           decaf=decaf,
                           ice=ice,
                           sweet=sweet)


@app.route('/update_drink/<boba_id>', methods=["POST"])
def update_drink(boba_id):
    """
    Update Drink in database
    """
    boba = mongo.db.boba
    boba.update({'_id': ObjectId(boba_id)},
                {
                 'drink_name': request.form.get('drink_name'),
                 'drink_type': request.form.get('drink_type'),
                 'tea_type': request.form.get('tea_type'),
                 'decaf': request.form.get('decaf'),
                 'top': request.form.get('top'),
                 'sweet': request.form.get('sweet'),
                 'ice': request.form.get('ice')
                })
    return redirect(url_for('get_drink'))


@app.route('/delete_drink/<boba_id>')
def delete_drink(boba_id):
    """
    Delete Drink From Database
    """
    mongo.db.boba.remove({'_id': ObjectId(boba_id)})
    return redirect(url_for('get_drink'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
