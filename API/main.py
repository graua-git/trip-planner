from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt
from datetime import datetime, timedelta

from Endpoints.QueryFunctions.create import create
from Endpoints.QueryFunctions.read import read
from Endpoints.QueryFunctions.update import update
from Endpoints.QueryFunctions.delete import delete
from Endpoints.QueryFunctions.validate import validate

ALL = "all"
ONE = "one"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cMIWy0a1M7iZAf1LpYtHAKGl=2xmX5ex97qRSl9Z4ec9Xhy2KVAgy7ZUaPciJPSbruSB?'

# Add Access for web app
CORS(app)
CORS(app, origins=['http://localhost:3000'])

# ---------------------------------- API END POINTS ----------------------------------
# ----------------------- Users -----------------------
@app.route('/users', methods=['GET'])
def read_users():
    sql = "SELECT user_id, email, first_name, last_name FROM Users"
    headers = ['user_id', 'email', 'first_name', 'last_name']
    return read(sql, headers)

@app.route('/user', methods=['GET'])
def get_user():
    # Validate token
    user_id = validate(request)
    if not isinstance(user_id, int):
        return user_id
    
    # Query database
    sql = f"SELECT user_id, email, first_name, last_name FROM Users WHERE user_id = {user_id}"
    headers = ['user_id', 'email', 'first_name', 'last_name']
    return read(sql, headers, ONE)

@app.route('/login', methods=['POST'])
def login():
    # Validate User
    user = request.get_json()
    sql = f"SELECT user_id FROM Users WHERE email = '{user['email']}' AND password = '{user['password']}'"
    headers = ['user_id']
    try:
        user_id = read(sql, headers, ONE)['user_id']
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    # Generate Token
    expires = datetime.utcnow() + timedelta(hours=1)
    payload = {
        'user_id': user_id,
        'expires': expires.isoformat()
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return jsonify({'token': token})

@app.route('/create-account', methods=['POST'])
def create_user():
    return create(request.get_json(), "Users")
    
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return update(request.get_json(), "Users", user_id)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return delete(f"DELETE FROM Users WHERE user_id = {user_id}")

# ----------------------- Trips -----------------------
@app.route('/trips', methods=['GET'])
def read_trips():
    sql = "SELECT * FROM Trips"
    headers = ['trip_id', 'name', 'start_date', 'end_date']
    return read(sql, headers)

@app.route('/mytrips', methods=['GET'])
def read_my_trips():
    # Validate token
    user_id = validate(request)
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

@app.route('/trips', methods=['POST'])
def create_trip():
    return create(request.get_json(), "Trips")

@app.route('/trips/<int:trip_id>', methods=['PUT'])
def update_trip(trip_id):
    return update(request.get_json(), "Trips", trip_id)

# -------------------- Memberships --------------------
@app.route('/memberships', methods=['GET'])
def read_memberships():
    sql = "SELECT membership_id, CONCAT(first_name, ' ', last_name) AS participant_name, email, name AS trip, owner \
            FROM Memberships \
            JOIN Users ON Users.user_id = Memberships.user \
            JOIN Trips on Trips.trip_id = Memberships.trip"
    headers = ['membership_id', 'participant_name', 'email', 'trip', 'owner']
    return read(sql, headers)

@app.route('/memberships', methods=['POST'])
def create_membership():
    return create(request.get_json(), "Memberships")

@app.route('/memberships/<int:membership_id>', methods=['PUT'])
def update_membership(membership_id):
    return update(request.get_json(), "Memberships", membership_id)

# ----------------------- Tasks -----------------------
@app.route('/tasks', methods=['GET'])
def read_tasks():
    sql = "SELECT * FROM Tasks"
    headers = ['task_id', 'name', 'trip', 'assignee', 'created_by', 'date_created', 'time_created', 'due_date', 'due_time']
    return read(sql, headers)

@app.route('/tasks', methods=['POST'])
def create_task():
    return create(request.get_json(), "Tasks")

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    return update(request.get_json(), "Tasks", task_id)

# --------------------- Expenses ----------------------
@app.route('/expenses', methods=['GET'])
def read_expenses():
    sql = "SELECT * FROM Expenses"
    headers = ['expense_id', 'name', 'trip', 'owed_to', 'owed_by', 'date_created', 'time_created', 'amount', 'settled']
    return read(sql, headers)

@app.route('/expenses', methods=['POST'])
def create_expense():
    return create(request.get_json(), "Expenses")

@app.route('/expenses/<int:expense_id>', methods=['PUT'])
def update_expense(expense_id):
    return update(request.get_json(), "Expenses", expense_id)

# ---------------------- Events -----------------------
@app.route('/events', methods=['GET'])
def read_events():
    sql = "SELECT * FROM Events"
    headers = ['event_id', 'name', 'trip', 'created_by', 'from_date', 'from_time', 'to_date', 'to_time']
    return read(sql, headers)

@app.route('/events', methods=['POST'])
def create_event():
    return create(request.get_json(), "Events")

@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    return update(request.get_json(), "Events", event_id)

# ----------------------------------- DRIVER CODE ------------------------------------
if __name__ == '__main__':
    app.run(debug=True)