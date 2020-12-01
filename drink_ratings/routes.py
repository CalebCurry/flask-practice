from drink_ratings import app
from flask import render_template, abort, url_for


drinks = [
    {
        'id': 0,
        'name': 'Black Cherry',
        'rating': 0,
        'content': 'This tastes like that one icecream.This tastes like that one icecream.',
        'src': 'https://image-cdn.symphonycommerce.com/images/sites/zevia/1548198074952_-601754611584738134.1200w.png'
    },
    {
        'id': 1,
        'name': 'Grape',
        'rating': 10,
        'content': 'Grapes yeeeeeett.',
        'src': 'https://image-cdn.symphonycommerce.com/images/sites/zevia/1548198170455_4685159556406169821.1200w.png'
        #'src': 'https://www.zevia.com/sites/default/files/2019-07/GrapeNR-1.png'
    },
]


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="404"), 404


@app.route('/')
def hello_world():
    return "hello World"


@app.route('/drinks')
def get_drinks():
    # return jsonify({'drinks': drinks})
    return render_template("drinks.html", drinks=drinks)


"""
@app.route("/drinks/new", methods=['GET', 'POST'])
def new_post():
    form = DrinkForm()
    if form.validate_on_submit():
        drink = Drink(name=form.title.data,
                    rating=form.content.data)
        db.session.add(drink)
        db.session.commit()
        flash('Your drink has been created!', 'success')
        return redirect(url_for('drinks'))
    return render_template('create_drink.html', title='New Drink',
                           form=form, legend='New Drink Legend?')
"""

# in my research on singular vs plural names for retrieving individual resources.
# I found this - https://stackoverflow.com/questions/6845772/rest-uri-convention-singular-or-plural-name-of-resource-while-creating-it
# I then saw the URL and saw that it said questions/6845772
# so plural it is with a passed in ID


@app.route('/drinks/<id>')
def get_rating(id):

    drink = None

    for d in drinks:
        if int(d.get('id')) == int(id):
            drink = d
    if drink is None:
        abort(404, description="Resource not found")
    return render_template("drink.html", title=drink.get('name'), drink=drink)
