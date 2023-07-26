from flask import Flask
from flask_restful import Api, Resource
import mysql.connector

app = Flask(__name__)
api = Api(app)

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='triplannerdb'
)
cursor = connection.cursor()

class HelloWorld(Resource):
    def get(self, name, test):
        return {"data": "Hello World!", "name": name, "test": test}
    
class Users(Resource):
    def get(self):
        cursor.execute("SELECT first_name, last_name FROM Users")
        return cursor.fetchall()

class Trips(Resource):
    def get(self):
        cursor.execute("SELECT name FROM Trips")
        return cursor.fetchall()
    
api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")
api.add_resource(Users, "/users")
api.add_resource(Trips, "/trips")

if __name__ == "__main__":
    app.run(debug=True)