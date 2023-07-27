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

# ------------------------------------ END POINTS ------------------------------------

# ----------------------- Users -----------------------
@app.route('/users', methods=['GET'])
def read_users():
    sql = "SELECT user_id, email, first_name, last_name FROM Users"
    cursor.execute(sql)
    return cursor.fetchall()

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
    cursor.execute(sql, val)
    db.commit()
    return jsonify({'message': "Record updated successfully"})

# ----------------------- Trips -----------------------
@app.route('/trips', methods=['GET'])
def read_trips():
    sql = "SELECT * FROM Trips"
    cursor.execute(sql)
    return cursor.fetchall()

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
    cursor.execute(sql, val)
    db.commit()
    return jsonify({'message': "Record updated successfully"})

# -------------------- Memberships --------------------
@app.route('/memberships', methods=['GET'])
def read_memberships():
    sql = "SELECT membership_id, CONCAT(first_name, ' ', last_name) AS participant_name, email, name AS trip, owner \
            FROM Memberships \
            JOIN Users ON Users.user_id = Memberships.user \
            JOIN Trips on Trips.trip_id = Memberships.trip"
    cursor.execute(sql)
    return cursor.fetchall()

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
    print(sql, val)
    cursor.execute(sql, val)
    db.commit()
    return jsonify({'message': "Record updated successfully"})

# ----------------------- Tasks -----------------------
# --------------------- Expenses ----------------------
# ---------------------- Events -----------------------

if __name__ == '__main__':
    app.run(debug=True)