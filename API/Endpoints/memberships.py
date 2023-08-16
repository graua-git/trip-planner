from flask import Blueprint, request, jsonify

from Endpoints.crud import create, read, update, delete
from Endpoints.token import validate_token, generate_token

memberships_bp = Blueprint('memberships', __name__)

@memberships_bp.route('/read-all', methods=['GET'])
def read_memberships():
    sql = "SELECT membership_id, CONCAT(first_name, ' ', last_name) AS participant_name, email, name AS trip, owner \
            FROM Memberships \
            JOIN Users ON Users.user_id = Memberships.user \
            JOIN Trips on Trips.trip_id = Memberships.trip"
    headers = ['membership_id', 'participant_name', 'email', 'trip', 'owner']
    return read(sql, headers)

@memberships_bp.route('/create', methods=['POST'])
def create_membership():
    return create(request.get_json(), "Memberships")

@memberships_bp.route('/update/<int:membership_id>', methods=['PUT'])
def update_membership(membership_id):
    return update(request.get_json(), "Memberships", membership_id)