from flask import Flask, request, jsonify
from flask_cors import CORS

from Endpoints.crud import create, read, update, delete
from Endpoints.users import users_bp
from Endpoints.trips import trips_bp
from Endpoints.memberships import memberships_bp
from Endpoints.tasks import tasks_bp

ALL = "all"
ONE = "one"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cMIWy0a1M7iZAf1LpYtHAKGl=2xmX5ex97qRSl9Z4ec9Xhy2KVAgy7ZUaPciJPSbruSB?'

# Add Access for web app
CORS(app)
CORS(app, resources={r"/*": {'origins': 'http://localhost:3000'}})

# Blueprints
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(trips_bp, url_prefix='/trips')
app.register_blueprint(memberships_bp, url_prefix='/memberships')
app.register_blueprint(tasks_bp, url_prefix='/tasks')


# --------------------- Expenses ----------------------

# ---------------------- Events -----------------------
@app.route('/events', methods=['GET'])
def read_events():
    sql = "SELECT * FROM Events"
    headers = ['event_id', 'name', 'trip', 'created_by', 'from_date', 'from_time', 'to_date', 'to_time']
    return read(sql, headers)

@app.route('/events', methods=['POST'])
def create_event():
    return create(request.get_json(), "Events")

@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    return update(request.get_json(), "Events", event_id)

# ----------------------------------- DRIVER CODE ------------------------------------
if __name__ == '__main__':
    app.run(debug=True)