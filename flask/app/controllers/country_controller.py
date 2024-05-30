from flask import jsonify, request
from app.init import app, db, auth
from app.models.country import Country

@app.route('/')
def hello():
    return "Hello World!"

# @app.route('/countries', methods=['GET'])
@app.get('/countries')
# @auth.login_required()
def countries():
    fields = ['country_id', 'country_name', 'capital', 'area']
    api_data = []
    kwargs = {}
    countries = Country.query.all()
    for country in countries:
        # print(country)
        for field in fields:
            value = getattr(country, field)
            kwargs[field] = value
        api_data.append(kwargs)
        kwargs = {}
    return jsonify(api_data)

@app.route('/country_details/<int:country_id>', methods=["GET"])
def country_details(country_id: int):
    fields = ['country_id', 'country_name', 'capital', 'area']
    kwargs = {}
    country = Country.query.filter_by(country_id=country_id).first()
    if country:
        for field in fields:
            value = getattr(country, field)
            kwargs[field] = value
        return jsonify(kwargs)
    return jsonify("That country does not exist!"), 404

# @app.route('/add_country', methods=["POST"])
@app.post('/add_country')
def add_country():
    country_name = request.form['country_name']
    check_country = Country.query.filter_by(country_name=country_name).first()
    if check_country:
        return jsonify("The country by that name exist in DB"), 409
    capital = request.form['capital']
    area = request.form['area']
    new_country = Country(country_name=country_name, capital=capital, area=area)
    db.session.add(new_country)
    db.session.commit()
    return jsonify(message="You added a new country."), 201

@app.route('/add_country1', methods=["POST"])
def add_country1():
    data = request.get_json()
    if not data:
        return jsonify("Invalid or missing JSON data"), 400
    country_name = data.get('country_name')
    check_country = Country.query.filter_by(country_name=country_name).first()
    if check_country:
        return jsonify("The country by that name exist in DB"), 409
    capital = data.get('capital')
    area = data.get('area')
    new_country = Country(country_name=country_name, capital=capital, area=area)
    db.session.add(new_country)
    db.session.commit()
    return jsonify(message="You added a new country."), 201

@app.route('/countries/<int:country_id>', methods=['PATCH'])
def update_country(country_id):
    data = request.get_json()
    country = Country.query.filter_by(country_id=country_id).first()
    if not country:
        return jsonify(message="Country not found"), 404
    if 'country_name' in data:
        country.country_name = data['country_name']
    if 'capital' in data:
        country.country_name = data['capital']
    if 'area' in data:
        country.country_name = data['area']
    db.session.commit()
    return jsonify({"message": "Country updated successfully", "country_id":country_id}), 200

@app.route('/remove_country/<int:country_id>', methods=['DELETE'])
def remove_country(country_id):
    country = Country.query.filter_by(country_id=country_id).first()
    if not country:
        return jsonify(message="Country not found"), 404
    db.session.delete(country)
    db.session.commit()
    return jsonify(message=f"You deleted a country with id of {country_id}"), 202   