# API Endpoints related to the Expenses table
from flask_restful import Resource
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='triplannerdb'
)
cursor = connection.cursor()

class ReadExpenses(Resource):
    def get(self):
        cursor.execute("SELECT * FROM Expenses")
        return cursor.fetchall()