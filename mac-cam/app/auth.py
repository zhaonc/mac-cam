from flask import request, Response
from functools import wraps
import settings


def check_auth(username, password):
    return username == settings.AUTH_USERNAME and password == settings.AUTH_PASSWORD


def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return Response(
                'Please login.', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'}
            )

        return f(*args, **kwargs)

    return decorated
