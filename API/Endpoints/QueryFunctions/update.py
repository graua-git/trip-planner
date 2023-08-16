from flask import jsonify
from Endpoints.QueryFunctions.db_connetion import db, cursor

def update(entry: dict, table: str, id: int) -> dict:
    """
    UPDATE Query
    entry: JSON Object representing row to insert
    table: table to insert object into
    id: id# of object to update
    returns: response message from MySQL
    """
    try:
        id_name = table.lower()[:-1] + "_id"
        end = f" WHERE {id_name} = {id}"
        sql = f"UPDATE {table} SET "
        for key, val in entry.items():
            if isinstance(val, str):
                val = "'" + val + "'"
            sql += str(key) + " = " + str(val) + ", "
        sql = sql[:-2] + end
        print(sql)
        cursor.execute(sql)
        db.commit()
        return jsonify({'message': "Record updated successfully"}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
