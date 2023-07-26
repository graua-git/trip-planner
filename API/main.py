from flask import Flask
from flask_restful import Api, Resource
import mysql.connector

app = Flask(__name__)
api = Api(app)

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='tripplannerdb'
)

class HelloWorld(Resource):
    def get(self, name, test):
        return {"data": "Hello World!", "name": name, "test": test}
    
api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")

if __name__ == "__main__":
    app.run(debug=True)