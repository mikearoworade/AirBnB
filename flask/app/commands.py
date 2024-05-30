from app.init import app, db
from app.models.country import Country
from app.models.user import User

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