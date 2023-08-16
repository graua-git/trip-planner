from flask import Blueprint, request

from Endpoints.crud import create, read, update, delete
from Endpoints.token import validate_token

events_bp = Blueprint('events', __name__)

@events_bp.route('/events', methods=['GET'])
def read_events():
    sql = "SELECT * FROM Events"
    headers = ['event_id', 'name', 'trip', 'created_by', 'from_date', 'from_time', 'to_date', 'to_time']
    return read(sql, headers)

@events_bp.route('/events', methods=['POST'])
def create_event():
    return create(request.get_json(), "Events")

@events_bp.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    return update(request.get_json(), "Events", event_id)
