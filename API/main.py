from flask import Flask
from flask_restful import Api, Resource

import Resources.Users as Users
import Resources.Trips as Trips
import Resources.Memberships as Memberships
import Resources.Tasks as Tasks
import Resources.Expenses as Expenses
import Resources.Events as Events

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self, name, test):
        return {"data": "Hello World!", "name": name, "test": test}

# Read Queries
api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")
api.add_resource(Users.ReadUsers, "/users")
api.add_resource(Trips.ReadTrips, "/trips")
api.add_resource(Memberships.ReadMemberships, "/memberships")
api.add_resource(Tasks.ReadTasks, "/tasks")
api.add_resource(Expenses.ReadExpenses, "/expenses")
api.add_resource(Events.ReadEvents, "/events")

if __name__ == "__main__":
    app.run(debug=True)