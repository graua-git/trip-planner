from flask import jsonify
from Endpoints.QueryFunctions.db_connetion import db, cursor

def delete(sql: str) -> dict:
    """
    DELETE Query
    sql: query
    returns: list of lists representing table
    """
    try:
        cursor.execute(sql)
        db.commit()
        return jsonify({'message': str(cursor.rowcount) + " record(s) deleted"}), 200
    except Exception as e:
            return jsonify({'error': str(e)}), 500
