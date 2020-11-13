from flask import Flask
from flask import jsonify
from flask import render_template
application = Flask(__name__)
app = application

drinks = {
    0: {
        'name': 'Black Cherry',
        'rating': 0
    },
    1: {
        'name': 'Grape',
        'rating': 10
    }
}


@app.route('/')
def hello_world():
    return "hello World"


@app.route('/drinks')
def get_drinks():
    # return jsonify({'drinks': drinks})
    return render_template("drinks.html", drinks=drinks)


@app.route('/drinks/<id>')
def get_rating(id):
    # this needs to be an int.
    # return drinks.get(int(id)) # for json
    return render_template("drink.html", drink=drinks.get(int(id)))
