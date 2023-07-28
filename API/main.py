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
def parse_json(entry: dict) -> (str, str, list):
    """
    Parses JSON object into strings to use for queries
    entry: JSON Object representing row
    returns:
        keys_str: string representing keys (key1, key2, key3, ...)
        vals_str: string representing values as %s (%s, %s, %s, ...)
        vals_data: list of values [val1, val2, val3, ...]
    """
    keys_str = "("
    vals_str = "("
    vals_data = []
    for key, val in entry.items():
        keys_str += key + ", "
        vals_str += "%s, "
        vals_data.append(val)
    keys_str = keys_str[:-2] + ")"
    vals_str = vals_str[:-2] + ")"
    return (keys_str, vals_str, vals_data)

def read(sql: str) -> list:
    """
    SELECT Query
    sql: query
    returns: list of lists representing table
    """
    cursor.execute(sql)
    return cursor.fetchall()

def create(entry: dict, table: str) -> dict:
    """
    INSERT INTO Query
    entry: JSON Object representing row to insert
    table: table to insert object into
    returns: response message for MySQL
    """
    keys_str = "("
    vals_str = "("
    vals_data = []
    for key, val in entry.items():
        keys_str += key + ", "
        vals_str += "%s, "
        vals_data.append(val)
    keys_str = keys_str[:-2] + ")"
    vals_str = vals_str[:-2] + ")"
    sql = f"INSERT INTO {table} " + keys_str + " VALUES " + vals_str
    cursor.execute(sql, vals_data)
    db.commit()
    return jsonify({'message': "Record updated successfully"})
    
# ---------------------------------- API END POINTS ----------------------------------
# ----------------------- Users -----------------------
@app.route('/users', methods=['GET'])
def read_users():
    return(read("SELECT user_id, email, first_name, last_name FROM Users"))

@app.route('/users', methods=['POST'])
def create_user():
    try:
        user = request.get_json()
        return create(user, "Users")
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ----------------------- Trips -----------------------
@app.route('/trips', methods=['GET'])
def read_trips():
    return(read("SELECT * FROM Trips"))

@app.route('/trips', methods=['POST'])
def create_trip():
    try:
        trip = request.get_json()
        return create(trip, "Trips")
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# -------------------- Memberships --------------------
@app.route('/memberships', methods=['GET'])
def read_memberships():
    return(read("SELECT membership_id, CONCAT(first_name, ' ', last_name) AS participant_name, email, name AS trip, owner \
            FROM Memberships \
            JOIN Users ON Users.user_id = Memberships.user \
            JOIN Trips on Trips.trip_id = Memberships.trip"))

@app.route('/memberships', methods=['POST'])
def create_membership():
    try:
        membership = request.get_json()
        return create(membership, "Memberships")
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ----------------------- Tasks -----------------------
@app.route('/tasks', methods=['GET'])
def read_tasks():
    return(read("SELECT * FROM Tasks"))

@app.route('/tasks', methods=['POST'])
def create_task():
    try:
        task = request.get_json()
        return create(task, "Tasks")
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# --------------------- Expenses ----------------------
@app.route('/expenses', methods=['GET'])
def read_expenses():
    return(read("SELECT * FROM Expenses"))

@app.route('/expenses', methods=['POST'])
def create_expense():
    try:
        expense = request.get_json()
        return create(expense, "Expenses")
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ---------------------- Events -----------------------
@app.route('/events', methods=['GET'])
def read_events():
    return read("SELECT * FROM Events")

@app.route('/events', methods=['POST'])
def create_event():
    try:
        event = request.get_json()
        return create(event, "Events")
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ----------------------------------- DRIVER CODE ------------------------------------
if __name__ == '__main__':
    app.run(debug=True)