from drink_ratings import app, jwt, bcrypt, db
from flask import render_template, abort, url_for, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import jwt
from drink_ratings.models import Testimonial


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
    return render_template('404.html', error=e, title="Page Not Found"), 404


testimonials = [
    {
        'id': 10,
        'name': 'Connor',
        'message': 'Your courses helped me land a job at McDonalds!'
    },
    {
        'id': 35,
        'name': 'Sarah',
        'message': 'Never have I understood OOP until now.'
    },
    {
        'id': 43,
        'name': 'John',
        'message': 'I watched all 200 hours straight!'
    },
]


@app.route('/api/testimonials')
def get_testimonials():
    testimonials = Testimonial.query.all()
    return jsonify({'testimonials': testimonials})


@app.route('/api/testimonials/<id>')
def get_testimonial(id):
    testimonial = Testimonial.query.get(id)

    if testimonial:
        return jsonify(testimonial)

    return {}


@app.route('/api/testimonials', methods=['POST'])
def add_testimonial():
    data = request.get_json()
    testimonial = Testimonial(name=data.get(
        'name'), testimonial=data.get('testimonial'))
    db.session.add(testimonial)
    db.session.commit()
    return jsonify(testimonial.id)


@app.route('/')
@app.route('/testimonials')
def show_testimonials():
    return render_template('index.html', testimonials=testimonials)


@app.route('/testimonials/<id>')
def show_testimonial(id):

    for testimonial in testimonials:
        if testimonial.get('id') == int(id):
            return render_template('testimonial.html', testimonial=testimonial)
    abort(404)

    '''
    drink = None

    for d in drinks:
        if int(d.get('id')) == int(id):
            drink = d
    if drink is None:
        abort(404, description="Resource not found")
    return render_template("drink.html", title=drink.get('name'), drink=drink)
    '''


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


@app.route('/notpass')
def notpass():
    pw_hash = bcrypt.generate_password_hash('passwordtest')
    return jsonify({'pw_hash': str(pw_hash)})


@app.route('/api/testimonials')
def get_testminonials():
    return {'testimonials': ["great", "its ok", "fantastic"]} + 5


@app.route('/api/string')
def string():
    return "this is a string"


@app.route('/test', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if username != 'test' or password != 'test':
        return jsonify({"msg": "Bad username or password"}), 401

    # Identity can be any data that is json serializable
    access_token = create_access_token(
        identity={'username': username, 'role': 'admin'})

    return jsonify(access_token=access_token), 200


@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    token = str.replace(request.headers.get('Authorization'), 'Bearer ', '')
    print("Token:", token)
    token = jwt.decode(token, None, None)
    print("Token decoded:", token)
    return jsonify(logged_in_as=current_user), 200


@app.route('/drinks/<id>')
def get_rating(id):

    drink = None

    for d in drinks:
        if int(d.get('id')) == int(id):
            drink = d
    if drink is None:
        abort(404, description="Resource not found")
    return render_template("drink.html", title=drink.get('name'), drink=drink)


@app.route('/drinks/<id>', methods=['POST'])
def update_rating(id):
    params = {
        'description': request.values.get('description'),
        'rating': request.get_json().get('rating')
    }
    return json.dumps(params)
