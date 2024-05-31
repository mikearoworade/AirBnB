from flask import Flask, jsonify, request
from sqlalchemy import Column, Integer, Float, String 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///country.db'
db = SQLAlchemy(app)


@app.route('/')
def hello_word():
    return 'Hello, World!'


@app.route('/simple')
def simple():
    return jsonify(text='Hello Simple World!', message='Hello Boss')


@app.route('/not_found')
def not_found():
    return jsonify(error='This route was not found'), 404


@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age > 18:
        return jsonify(message=f"Wecome {name}!!!")
    else:
        return jsonify(message=f"Sorry {name}, you are not old enough to access this API.")


@app.route('/api-variables/<string:name>/<int:age>')
def api_variables(name:str, age:int):
    if age > 18:
        return jsonify(message=f"Wecome {name}!!!")
    else:
        return jsonify(message=f"Sorry {name}, you are not old enough to access this API.")


# Database
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name =Column(String)
    last_name =Column(String)
    email = Column(String, unique=True)
    password = Column(String)


class Country(db.Model):
    __tablename__ = 'countries'
    country_id = Column(Integer, primary_key=True)
    country_name =Column(String)
    capital =Column(String)
    area = Column(Float)


@app.cli.command('db_create')
def db_create():
    db.create_all()
    print("Database Created..")


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print("Database dropped..")


@app.cli.command('db_seed')
def db_seed():
    usa = Country(country_name='USA', capital='Washington', area=23456)
    germany = Country(country_name='Germany', capital='Berlin', area=23459)
    db.session.add(usa)
    db.session.add(germany)

    test_user = User(first_name='Michael',
                     last_name='Aroworade',
                     email='mikearo@gmail.com',
                     password='mike123')
    db.session.add(test_user)
    db.session.commit()
    print("Datatbase Seeded...")


@app.cli.command('get_countries')
def get_countries():
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
    print(api_data)


@app.cli.command('get_country')
def get_country():
    country_id = 1
    fields = ['country_id', 'country_name', 'capital', 'area']
    kwargs = {}
    country = Country.query.filter_by(country_id=country_id).first()
    if country:
        for field in fields:
            value = getattr(country, field)
            kwargs[field] = value
        return kwargs


# @app.route('/countries', methods=['GET'])
@app.get('/countries',)
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


if __name__ == '__main__':
    app.run()
