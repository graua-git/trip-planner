from flask import Blueprint, request

from Endpoints.crud import create, read, update, delete
from Endpoints.token import validate_token

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/read-all', methods=['GET'])
def read_tasks():
    """
    Returns
    task_id | name | trip | assignee | created_by | date_created | time_created | due_date | due_time
    """
    sql = "SELECT * FROM Tasks"
    headers = ['task_id', 'name', 'trip', 'assignee', 'created_by', 'date_created', 'time_created', 'due_date', 'due_time']
    return read(sql, headers)

@tasks_bp.route('/create', methods=['POST'])
def create_task():
    """
    Creates task, requires info from json
    """
    return create(request.get_json(), "Tasks")

@tasks_bp.route('/update/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """
    Updates task, requires info from json
    """
    return update(request.get_json(), "Tasks", task_id)
