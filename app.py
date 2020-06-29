import os
from os import path
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length

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

# Get Drinks: View all drinks in database with the option to filter
@app.route('/get_drink', methods=['GET', 'POST'])
def get_drink():
    return render_template('drinks.html', boba=mongo.db.boba.find())

# Function to filter available drinks

# Add Drink form
@app.route("/add_drink")
def add_drink():
    return render_template('addDrink.html',
    boba=mongo.db.boba.find())

# Function to post user data to the database
@app.route('/insert_drink', methods=['POST'])
def insert_drink():
    boba = mongo.db.boba
    boba.insert_one(request.form.to_dict())
    return redirect(url_for('get_drink'))

# Edit Drink Form
@app.route('/edit_drink/<drink_id>', methods=["POST"])
def edit_drink(drink_id):
    boba = mongo.db.boba.find_one({"_id": ObjectId(drink_id)})
    drink_type = mongo.db.drinks.find()
    tea_type = mongo.db.teas.find()
    top = mongo.db.top.find()
    ice = mongo.db.ice.find()
    sweet = mongo.db.sweet.find()
    return render_template('editDrink.html',  boba=drink_id, drinks=drink_type, teas=tea_type, top=top, ice=ice, sweet=sweet)

# Update Drink in database
@app.route('/update_drink/<drink_name>', methods=["POST"])
def update_location(location_id):
    boba = mongo.db.boba
    boba.update({'_id': ObjectId(drink_id)},
        {
            'drink_name': request.form.get('drink_name'),
            'drink_type': request.form.get('drink_type'),
            'tea_type': request.form.get('tea_type'),
            'decaf': request.form.get('caffeine'),
            'top': request.form.get('topping'),
            'sweet': request.form.get('sweet_level'),
            'ice': request.form.get('ice')
        })
    return redirect(url_for('get_drink'))

# Delete Drink From Database
@app.route('/delete_drink/<drink_id>')
def delete_drink(drink_id):
    mongo.db.tasks.remove({'_id': ObjectId(drink_id)})
    return redirect(url_for('get_drink'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)
