from flask import Blueprint, request

from Endpoints.crud import create, read, update, delete
from Endpoints.token import validate_token

trips_bp = Blueprint('trips', __name__)

@trips_bp.route('/read-all', methods=['GET'])
def read_trips():
    sql = "SELECT * FROM Trips"
    headers = ['trip_id', 'name', 'start_date', 'end_date']
    return read(sql, headers)

@trips_bp.route('/mytrips', methods=['GET'])
def read_my_trips():
    # Validate token
    user_id = validate_token(request)
    if not isinstance(user_id, int):
        return user_id
    
    # Query database
    sql = f"SELECT name, start_date, end_date, organizer \
            FROM Trips \
            JOIN Memberships ON Memberships.trip = Trips.trip_id \
            JOIN Users ON Users.user_id = Memberships.user \
            JOIN (SELECT trip, owner, CONCAT(Users.first_name, ' ', Users.last_name) as organizer \
            FROM Memberships \
            JOIN Users ON Users.user_id = Memberships.user \
            WHERE owner = 1) as Owners ON  Trips.trip_id = Owners.trip \
            WHERE Users.user_id = {user_id}"
    headers = ['name', 'start_date', 'end_date', 'organizer']
    return read(sql, headers)

@trips_bp.route('/create', methods=['POST'])
def create_trip():
    return create(request.get_json(), "Trips")

@trips_bp.route('/update/<int:trip_id>', methods=['PUT'])
def update_trip(trip_id):
    return update(request.get_json(), "Trips", trip_id)