from flask import jsonify
import jwt
from key import read_key

def validate(request):
    """
    Decorator function to validate token from HTTP request
    request: HTTP request
    returns: int, user_id IF token is valid ELSE dict, message
    """
    token = request.headers.get('Authorization', 'NONE')
    
    if not token or not token.startswith('Bearer '):
        return jsonify({'message': 'Token is missing'}), 401
    token = token.replace('Bearer ', '')

    try:
        payload = jwt.decode(token, read_key(), algorithms=['HS256'])
        return payload.get('user_id')
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 401
    except jwt.DecodeError:
        return jsonify({'message': 'Invalid token'}), 401
