from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

ALL = "all"
ONE = "one"

app = Flask(__name__)

# Add Access for web app
CORS(app)
CORS(app, origins=['http://localhost:3000'])

# Create DB connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='triplannerdb'
)
cursor = db.cursor()

# --------------------------------- DATABASE QUERIES ---------------------------------
def parse_json(entry: dict) -> dict:
    """
    Parses JSON object into strings to use for queries
    entry: JSON Object representing row
    returns: dict
        keys_str: string representing keys "(key1, key2, key3, ...)"
        keys_data: list of keys [key1, key2, key3, ...]
        vals_str: string representing values as %s "(%s, %s, %s, ...)"
        vals_data: list of values [val1, val2, val3, ...]
    """
    keys_str, vals_str = "(", "("
    keys_li, vals_li = [], []
    for key, val in entry.items():
        keys_str += key + ", "
        keys_li.append(key)
        vals_str += "%s, "
        vals_li.append(val)
    keys_str = keys_str[:-2] + ")"
    vals_str = vals_str[:-2] + ")"
    return {
            'keys_str': keys_str, 
            'keys_li': keys_li,
            'vals_str': vals_str,
            'vals_li': vals_li
            }

def create(entry: dict, table: str) -> dict:
    """
    INSERT INTO Query
    entry: JSON Object representing row to insert
    table: table to insert object into
    returns: response message from MySQL
    """
    try:
        entry_dict = parse_json(entry)
        sql = f"INSERT INTO {table} " + entry_dict['keys_str'] + " VALUES " + entry_dict['vals_str']
        cursor.execute(sql, entry_dict['vals_li'])
        db.commit()
        return jsonify({'message': "Record updated successfully"}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def read(sql: str, headers: list, quantity: str = ALL) -> list:
    """
    SELECT Query
    sql: query
    headers: list of column names (str) in order
    returns: list of lists representing table
    quantity: "one" or "all"
    """
    try:
        cursor.execute(sql)
        table = cursor.fetchall()
        result = []
        for row in table:
            new_row = dict()
            for i, col in enumerate(row):
                new_row[headers[i]] = col
            result.append(new_row)
        if quantity == "one":
            return result[0]
        else:
            return result
    except Exception as e:
            return jsonify({'error': str(e)}), 500

def update(entry: dict, table: str, id: int) -> dict:
    """
    UPDATE Query
    entry: JSON Object representing row to insert
    table: table to insert object into
    id: id# of object to update
    returns: response message from MySQL
    """
    try:
        id_name = table.lower()[:-1] + "_id"
        end = f" WHERE {id_name} = {id}"
        sql = f"UPDATE {table} SET "
        for key, val in entry.items():
            if isinstance(val, str):
                val = "'" + val + "'"
            sql += str(key) + " = " + str(val) + ", "
        sql = sql[:-2] + end
        print(sql)
        cursor.execute(sql)
        db.commit()
        return jsonify({'message': "Record updated successfully"}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def delete(sql: str) -> dict:
    """
    DELETE Query
    sql: query
    returns: list of lists representing table
    """
    try:
        cursor.execute(sql)
        db.commit()
        return jsonify({'message': str(cursor.rowcount) + " record(s) deleted"}), 200
    except Exception as e:
            return jsonify({'error': str(e)}), 500

# ---------------------------------- API END POINTS ----------------------------------
# ----------------------- Users -----------------------
@app.route('/users', methods=['GET'])
def read_users():
    sql = "SELECT user_id, email, first_name, last_name FROM Users"
    headers = ['user_id', 'email', 'first_name', 'last_name']
    return read(sql, headers)

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    sql = f"SELECT user_id, email, first_name, last_name FROM Users WHERE user_id = {user_id}"
    headers = ['user_id', 'email', 'first_name', 'last_name']
    return read(sql, headers, ONE)

@app.route('/login', methods=['POST'])
def login():
    user = request.get_json()
    sql = f"SELECT user_id FROM Users WHERE email = '{user['email']}' AND password = '{user['password']}'"
    headers = ['user_id']
    return read(sql, headers)

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

@app.route('/mytrips/<int:user_id>', methods=['GET'])
def read_my_trips(user_id):
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
    app.run(debug=False)