from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta

from Endpoints.crud import create, read, update, delete
from Endpoints.token import validate_token, generate_token

user_bp = Blueprint('users', __name__)

@user_bp.route('/read-all', methods=['GET'])
def read_users():
    sql = "SELECT user_id, email, first_name, last_name FROM Users"
    headers = ['user_id', 'email', 'first_name', 'last_name']
    return read(sql, headers)

@user_bp.route('/read-one', methods=['GET'])
def get_user():
    # Validate token
    user_id = validate_token(request)
    if not isinstance(user_id, int):
        return user_id
    
    # Query database
    sql = f"SELECT user_id, email, first_name, last_name FROM Users WHERE user_id = {user_id}"
    headers = ['user_id', 'email', 'first_name', 'last_name']
    return read(sql, headers, 'one')

@user_bp.route('/login', methods=['POST'])
def login():
    # Validate User
    user = request.get_json()
    sql = f"SELECT user_id FROM Users WHERE email = '{user['email']}' AND password = '{user['password']}'"
    headers = ['user_id']
    try:
        user_id = read(sql, headers, 'one')['user_id']
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    # Generate Token
    token = generate_token(user_id)
    return jsonify({'token': token})

@user_bp.route('/create-account', methods=['POST'])
def create_user():
    return create(request.get_json(), "Users")
    
@user_bp.route('/update-user', methods=['PUT'])
def update_user(user_id):
    return update(request.get_json(), "Users", user_id)

@user_bp.route('/delete-user', methods=['DELETE'])
def delete_user(user_id):
    return delete(f"DELETE FROM Users WHERE user_id = {user_id}")