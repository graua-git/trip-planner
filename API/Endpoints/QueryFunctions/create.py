from flask import jsonify
from Endpoints.QueryFunctions.db_connetion import db, cursor
from Endpoints.QueryFunctions.parse_json import parse_json

def create(entry: dict, table: str) -> dict:
    """
    INSERT INTO Query
    entry: JSON Object representing row to insert
    table: table to insert object into
    returns: response message from MySQL
    """
    try:
        entry_dict = parse_json(entry)
        sql = f"INSERT INTO {table} " + entry_dict['keys_str'] + " VALUES " + entry_dict['vals_str']
        cursor.execute(sql, entry_dict['vals_li'])
        db.commit()
        return jsonify({'message': "Record updated successfully"}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
