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
