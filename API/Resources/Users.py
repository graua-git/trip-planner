# API Endpoints related to the Users table
from flask_restful import Api, Resource
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='triplannerdb'
)
cursor = connection.cursor()

class ReadUsers(Resource):
    def get(self):
        cursor.execute("SELECT email, first_name, last_name FROM Users")
        return cursor.fetchall()