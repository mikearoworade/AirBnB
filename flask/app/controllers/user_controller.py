from app.init import app, db, auth
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from flask_jwt_extended import create_access_token


@auth.verify_password
def verify_password(email, password):
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return True
    return False


@app.get('/users')
@auth.login_required
def user():
    fields = ['first_name', 'last_name', 'email', 'password']
    api_data = []
    kwargs = {}
    users = User.query.all()
    for user in users:
        # print(country)
        for field in fields:
            value = getattr(user, field)
            kwargs[field] = value
        api_data.append(kwargs)
        kwargs = {}
    return jsonify(api_data)

@app.post('/register')
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    new_user = User(first_name=data['first_name'],
                    last_name=data['last_name'],
                    email=data['email'],
                    password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message="Registered Successfully."), 201


@app.post('/login')
def login():
    data = request.get_json()
    if not data:
        return {"message": "Invalid or missing JSON data"}, 400
    email = data.get("email")
    password = data.get("password")
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return {"message": "Incorrect Username or password"}
    access_token = create_access_token(identity=email)
    return {"message": "Successful login", "access_token": access_token}