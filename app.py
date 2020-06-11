from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'byob_boba'
app.config["MONGO_URI"] = 'mongodb+srv://abru:<password>@cluster0-t8ogt.mongodb.net/test?retryWrites=true&w=majority'
mongo = PyMongo(app)

# Home Page
@app.route('/home')
def view_home():
    return render_template("index.html")

# Get Drinks: View all drinks in database with the option to filter
@app.route('/get_drinks', methods=['GET', 'POST'])
def get_drink():
    drinks_list = tea.db.drinks.find()
# Filter results
def search_drinks(search):
    drinks = []
    search_string = search.data['search']
    if search_string:
        if search.data['select'] == 'Drink Type':
            qry = db_session.query(Drinks, drink_type).filter(
                drink_type==drinks.drink_type).filter(
                    drink_type.contains(search_string))
            results = [item[0] for item in qry.all()]
        elif search.data['select'] == 'Tea Type':
            qry = db_session.query(Drinks).filter(
                Drinks.tea_type.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Toppings':
            qry = db_session.query(Drinks).filter(
                Drinks.toppings.contains(search_string))
            results = qry.all()
        else:
            qry = db_session.query(Drinks)
            results = qry.all()
    else:
        qry = db_session.query(Drinks)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Drinks(results)
        table.border = True
        return render_template('drinks.html', tea=mongo.db.drinks.find())


# Add Drink form
@app.route("/add_drink", methods=['POST'])
def add_drink():
    add = mongo.db.drinks
    drink.insert_one(request.form.to_dict())
    return redirect(url_for('get_drinks'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT'), debug=True)
