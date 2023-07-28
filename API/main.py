from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='triplannerdb'
)
cursor = db.cursor()

# --------------------------------- DATABASE QUERIES ---------------------------------
def create(sql, val):
    cursor.execute(sql, val)
    db.commit()
    return jsonify({'message': "Record updated successfully"})

def read(sql):
    cursor.execute(sql)
    return cursor.fetchall()

# ---------------------------------- API END POINTS ----------------------------------
# ----------------------- Users -----------------------
@app.route('/users', methods=['GET'])
def read_users():
    return(read("SELECT user_id, email, first_name, last_name FROM Users"))

@app.route('/users', methods=['POST'])
def create_user():
    # Data from POST request
    user = request.get_json()
    email = user.get('email')
    password = user.get('password')
    first_name = user.get('first_name')
    last_name = user.get('last_name')
    # Query database
    sql = "INSERT INTO Users (email, password, first_name, last_name) VALUES (%s, %s, %s, %s)"
    val = (email, password, first_name, last_name)
    return create(sql, val)

# ----------------------- Trips -----------------------
@app.route('/trips', methods=['GET'])
def read_trips():
    return(read("SELECT * FROM Trips"))

@app.route('/trips', methods=['POST'])
def create_trip():
    # Data from POST request
    trip = request.get_json()
    name = trip.get('name')
    start_date = trip.get('start_date')
    end_date = trip.get('end_date')
    # Query database
    sql = "INSERT INTO Trips (name, start_date, end_date) VALUES (%s, %s, %s)"
    val = (name, start_date, end_date)
    return create(sql, val)

# -------------------- Memberships --------------------
@app.route('/memberships', methods=['GET'])
def read_memberships():
    return(read("SELECT membership_id, CONCAT(first_name, ' ', last_name) AS participant_name, email, name AS trip, owner \
            FROM Memberships \
            JOIN Users ON Users.user_id = Memberships.user \
            JOIN Trips on Trips.trip_id = Memberships.trip"))

@app.route('/memberships', methods=['POST'])
def create_membership():
    # Data from POST request
    membership = request.get_json()
    user = membership.get('user')
    trip = membership.get('trip')
    owner = membership.get('owner')
    # Query database
    sql = "INSERT INTO Memberships (user, trip, owner) VALUES (%s, %s, %s)"
    val = (user, trip, owner)
    return create(sql, val)

# ----------------------- Tasks -----------------------
@app.route('/tasks', methods=['GET'])
def read_tasks():
    return(read("SELECT * FROM Tasks"))

@app.route('/tasks', methods=['POST'])
def create_task():
    # Data from POST request
    task = request.get_json()
    name = task.get('name')
    trip = task.get('trip')
    assignee = task.get('assignee')
    created_by = task.get('created_by')
    date_created = task.get('date_created')
    time_created = task.get('time_created')
    due_date = task.get('due_date')
    due_time = task.get('due_time')
    # Query database
    sql = "INSERT INTO Tasks (name, trip, assignee, created_by, date_created, time_created, due_date, due_time) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (name, trip, assignee, created_by, date_created, time_created, due_date, due_time)
    return create(sql, val)

# --------------------- Expenses ----------------------
@app.route('/expenses', methods=['GET'])
def read_expenses():
    return(read("SELECT * FROM Expenses"))

@app.route('/expenses', methods=['POST'])
def create_expense():
    # Data from POST request
    expense = request.get_json()
    name = expense.get('name')
    trip = expense.get('trip')
    owed_to = expense.get('owed_to')
    owed_by = expense.get('owed_by')
    date_created = expense.get('date_created')
    time_created = expense.get('time_created')
    amount = expense.get('amount')
    settled = expense.get('settled')
    # Query database
    sql = "INSERT INTO Expenses (name, trip, owed_to, owed_by, date_created, time_created, amount, settled) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (name, trip, owed_to, owed_by, date_created, time_created, amount, settled)
    return create(sql, val)

# ---------------------- Events -----------------------
@app.route('/events', methods=['GET'])
def read_events():
    return read("SELECT * FROM Events")

@app.route('/events', methods=['POST'])
def create_event():
    # Data from POST request
    event = request.get_json()
    print(event)
    name = event.get('name')
    trip = event.get('trip')
    created_by = event.get('created_by')
    from_date = event.get('from_date')
    from_time = event.get('from_time')
    to_date = event.get('to_date')
    to_time = event.get('to_time')
    # Query database
    sql = "INSERT INTO Events (name, trip, created_by, from_date, from_time, to_date, to_time) \
            VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (name, trip, created_by, from_date, from_time, to_date, to_time)
    return create(sql, val)

# ----------------------------------- DRIVER CODE ------------------------------------
if __name__ == '__main__':
    app.run(debug=True)