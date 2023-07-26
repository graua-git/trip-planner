# API Endpoints related to the Events table
from flask_restful import Resource
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='triplannerdb'
)
cursor = connection.cursor()

class ReadTasks(Resource):
    def get(self):
        cursor.execute("SELECT * FROM Tasks")
        return cursor.fetchall()