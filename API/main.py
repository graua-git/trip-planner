from flask import Flask
from flask_cors import CORS

from Endpoints.users import users_bp
from Endpoints.trips import trips_bp
from Endpoints.memberships import memberships_bp
from Endpoints.tasks import tasks_bp
from Endpoints.expenses import expenses_bp
from Endpoints.events import events_bp

app = Flask(__name__)

# Add Access for web app
CORS(app)
CORS(app, resources={r"/*": {'origins': 'http://localhost:3000'}})

# Blueprints
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(trips_bp, url_prefix='/trips')
app.register_blueprint(memberships_bp, url_prefix='/memberships')
app.register_blueprint(tasks_bp, url_prefix='/tasks')
app.register_blueprint(expenses_bp, url_prefix='/expenses')
app.register_blueprint(events_bp, url_prefix='/events')

if __name__ == '__main__':
    app.run(debug=True)
