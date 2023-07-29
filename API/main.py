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

def read(sql: str) -> list:
    """
    SELECT Query
    sql: query
    returns: list of lists representing table
    """
    try:
        cursor.execute(sql)
        return cursor.fetchall()
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
    return read("SELECT user_id, email, first_name, last_name FROM Users")

@app.route('/users', methods=['POST'])
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
    return read("SELECT * FROM Trips")

@app.route('/trips', methods=['POST'])
def create_trip():
    return create(request.get_json(), "Trips")

@app.route('/trips/<int:trip_id>', methods=['PUT'])
def update_trip(trip_id):
    return update(request.get_json(), "Trips", trip_id)

# -------------------- Memberships --------------------
@app.route('/memberships', methods=['GET'])
def read_memberships():
    return read("SELECT membership_id, CONCAT(first_name, ' ', last_name) AS participant_name, email, name AS trip, owner \
            FROM Memberships \
            JOIN Users ON Users.user_id = Memberships.user \
            JOIN Trips on Trips.trip_id = Memberships.trip")

@app.route('/memberships', methods=['POST'])
def create_membership():
    return create(request.get_json(), "Memberships")

@app.route('/memberships/<int:membership_id>', methods=['PUT'])
def update_membership(membership_id):
    return update(request.get_json(), "Memberships", membership_id)

# ----------------------- Tasks -----------------------
@app.route('/tasks', methods=['GET'])
def read_tasks():
    return read("SELECT * FROM Tasks")

@app.route('/tasks', methods=['POST'])
def create_task():
    return create(request.get_json(), "Tasks")

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    return update(request.get_json(), "Tasks", task_id)

# --------------------- Expenses ----------------------
@app.route('/expenses', methods=['GET'])
def read_expenses():
    return read("SELECT * FROM Expenses")

@app.route('/expenses', methods=['POST'])
def create_expense():
    return create(request.get_json(), "Expenses")

@app.route('/expenses/<int:expense_id>', methods=['PUT'])
def update_expense(expense_id):
    return update(request.get_json(), "Expenses", expense_id)

# ---------------------- Events -----------------------
@app.route('/events', methods=['GET'])
def read_events():
    return read("SELECT * FROM Events")

@app.route('/events', methods=['POST'])
def create_event():
    return create(request.get_json(), "Events")

@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    return update(request.get_json(), "Events", event_id)

# ----------------------------------- DRIVER CODE ------------------------------------
if __name__ == '__main__':
    app.run(debug=True)