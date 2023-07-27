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

# ------------------ Users ------------------
@app.route('/users', methods=['GET'])
def read_users():
    sql = "SELECT email, first_name, last_name FROM Users"
    cursor.execute(sql)
    return cursor.fetchall()

@app.route('/users', methods=['POST'])
def create_users():
    user = request.get_json()
    email = user.get('email')
    password = user.get('password')
    first_name = user.get('first_name')
    last_name = user.get('last_name')
    sql = "INSERT INTO Users (email, password, first_name, last_name) VALUES (%s, %s, %s, %s)"
    val = (email, password, first_name, last_name)
    cursor.execute(sql, val)
    db.commit()
    return jsonify({'message': "Record updated successfully"})

# ------------------ Trips ------------------
# --------------- Memberships ---------------
# ------------------ Tasks ------------------
# ---------------- Expenses -----------------
# ----------------- Events ------------------

if __name__ == '__main__':
    app.run(debug=True)