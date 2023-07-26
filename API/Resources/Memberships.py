# API Endpoints related to the Memberships table
from flask_restful import Api, Resource
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
        cursor.execute("SELECT * FROM Memberships")
        return cursor.fetchall()