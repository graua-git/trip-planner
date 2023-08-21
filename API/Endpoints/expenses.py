from flask import Blueprint, request

from Endpoints.crud import create, read, update, delete
from Endpoints.token import validate_token

expenses_bp = Blueprint('expenses', __name__)

@expenses_bp.route('/read-all', methods=['GET'])
def read_expenses():
    """
    Returns
    expense_id | name | trip | owed_to | owed_by | date_created | time_created | amount | settled
    """
    sql = "SELECT * FROM Expenses"
    headers = ['expense_id', 'name', 'trip', 'owed_to', 'owed_by', 'date_created', 'time_created', 'amount', 'settled']
    return read(sql, headers)

@expenses_bp.route('/create', methods=['POST'])
def create_expense():
    """
    Creates expense, requires info from json
    """
    return create(request.get_json(), "Expenses")

@expenses_bp.route('/update/<int:expense_id>', methods=['PUT'])
def update_expense(expense_id):
    """
    Updates expense, requires info from json
    """
    return update(request.get_json(), "Expenses", expense_id)
