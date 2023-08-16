from flask import Flask, request, jsonify
from flask_cors import CORS

from Endpoints.crud import create, read, update, delete
from Endpoints.users import users_bp
from Endpoints.trips import trips_bp

ALL = "all"
ONE = "one"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cMIWy0a1M7iZAf1LpYtHAKGl=2xmX5ex97qRSl9Z4ec9Xhy2KVAgy7ZUaPciJPSbruSB?'

# Add Access for web app
CORS(app)
CORS(app, resources={r"/*": {'origins': 'http://localhost:3000'}})

# ---------------------------------- API END POINTS ----------------------------------
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(trips_bp, url_prefix='/trips')


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