from app.init import auth
from flask import jsonify
from app.models.user import User
from werkzeug.security import check_password_hash


@auth.verify_password
def verify_password(email, password):
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return True
    return jsonify({"message": "This is a public route"})
