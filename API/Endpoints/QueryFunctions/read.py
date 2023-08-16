from flask import jsonify
from Endpoints.QueryFunctions.db_connetion import cursor

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
