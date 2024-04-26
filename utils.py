from flask import make_response, request
from functools import wraps

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization

        if auth and auth.username == "user" and auth.password == "pass":
            return f(*args, **kwargs)
        return make_response("Access Denied!" , 401, {'WWW-Authenticate':'Basic realm="Login required!"'})
    
    return decorated