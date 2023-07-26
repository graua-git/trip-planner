# API Endpoints related to the Memberships table
from flask_restful import Resource
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='triplannerdb'
)
cursor = connection.cursor()

class ReadMemberships(Resource):
    def get(self):
        cursor.execute("SELECT membership_id, CONCAT(first_name, ' ', last_name) AS participant_name, email, name AS trip, owner \
                        FROM Memberships \
                        JOIN Users ON Users.user_id = Memberships.user \
                        JOIN Trips on Trips.trip_id = Memberships.trip")
        return cursor.fetchall()