# API Endpoints related to the Users table
from flask_restful import Resource
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='triplannerdb'
)
cursor = connection.cursor()

class CreateUsers(Resource):
    def get(self, email, password, first_name, last_name):
        sql = "INSERT INTO Users (email, password, first_name, last_name) VALUES (%s, %s, %s, %s)"
        val = (email, password, first_name, last_name)
        cursor.execute(sql, val)
        connection.commit()

class ReadUsers(Resource):
    def get(self):
        cursor.execute("SELECT email, first_name, last_name FROM Users")
        return cursor.fetchall()
