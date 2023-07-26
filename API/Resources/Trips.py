# API Endpoints related to the Trips table
from flask_restful import Resource
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='triplannerdb'
)
cursor = connection.cursor()

class ReadTrips(Resource):
    def get(self):
        cursor.execute("SELECT * FROM Trips")
        return cursor.fetchall()
