from flask import request
from . import api
from app.models import User


@api.route('/')
def index():
    return "Hello this is the API"

# @api.route('/users')
# def get_users():
#     users = User.query.all()
#     return [u.to_dict() for u in users]

@api.route('/users/<int:user_id>')
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return user.to_dict()

@api.route('/users', methods=['POST'])
def create_user():
    if not request.is_json:
        return {'error': 'Your request content-type must be application/json'}, 400
    data = request.json
    for field in ['username', 'email', 'password']:
        if field not in data:
            return{'error': f"{field} must be in request body"}, 400

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    new_user = User(username = username, email=email, password = password)

    return new_user.to_dict(), 201
