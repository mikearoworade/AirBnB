from app import auth
from app.models.user import User
from werkzeug.security import check_password_hash

@auth.verify_password
def verify_password(email, password):
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return False
    return True