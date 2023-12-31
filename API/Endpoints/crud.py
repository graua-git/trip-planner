from flask import jsonify
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='triplannerdb'
)
cursor = db.cursor()

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
    
def read(sql: str, headers: list, quantity: str = 'all') -> list:
    """
    SELECT Query
    sql: query
    headers: list of column names (str) in order
    returns: list of lists representing table
    quantity: "one" or "all"
    """
    try:
        cursor.execute(sql)
        table = cursor.fetchall()
        result = []
        for row in table:
            new_row = dict()
            for i, col in enumerate(row):
                new_row[headers[i]] = col
            result.append(new_row)
        if quantity == "one":
            return result[0]
        else:
            return result
    except Exception as e:
            return jsonify({'error': str(e)}), 500

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

def parse_json(entry: dict) -> dict:
    """
    Parses JSON object into strings to use for queries
    entry: JSON Object representing row
    returns: dict
        keys_str: string representing keys "(key1, key2, key3, ...)"
        keys_data: list of keys [key1, key2, key3, ...]
        vals_str: string representing values as %s "(%s, %s, %s, ...)"
        vals_data: list of values [val1, val2, val3, ...]
    """
    keys_str, vals_str = "(", "("
    keys_li, vals_li = [], []
    for key, val in entry.items():
        keys_str += key + ", "
        keys_li.append(key)
        vals_str += "%s, "
        vals_li.append(val)
    keys_str = keys_str[:-2] + ")"
    vals_str = vals_str[:-2] + ")"
    return {
            'keys_str': keys_str, 
            'keys_li': keys_li,
            'vals_str': vals_str,
            'vals_li': vals_li
            }
