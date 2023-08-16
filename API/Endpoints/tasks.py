from flask import Blueprint, request

from Endpoints.crud import create, read, update, delete
from Endpoints.token import validate_token

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['GET'])
def read_tasks():
    sql = "SELECT * FROM Tasks"
    headers = ['task_id', 'name', 'trip', 'assignee', 'created_by', 'date_created', 'time_created', 'due_date', 'due_time']
    return read(sql, headers)

@tasks_bp.route('/tasks', methods=['POST'])
def create_task():
    return create(request.get_json(), "Tasks")

@tasks_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    return update(request.get_json(), "Tasks", task_id)
