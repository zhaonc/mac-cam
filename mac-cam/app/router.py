from flask import Flask, render_template, request, Response, jsonify, make_response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

import errors
import settings
from auth import require_auth
from camera import Camera
from logger import LOGGER

router = Flask(__name__)

limiter = Limiter(
    router,
    key_func=get_remote_address,
    default_limits=settings.LIMIT_DEFAULT,
    headers_enabled=True
)


def stream(camera):
    while True:
        frame = camera.get()
        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n'
        )


@router.before_request
def debug_log():
    LOGGER.debug('Received request: {}'.format(str(request.__dict__)))


@router.route('/')
@require_auth
def index():
    return render_template('index.html')


@router.route('/feed')
@require_auth
def feed():
    return Response(
        stream(Camera()),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


@router.errorhandler(errors.GenericError)
def handle_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@router.errorhandler(429)
def handle_limit_hit(error):
    return make_response(
        jsonify(error="Limit exceeded %s" % error.description),
        429
    )
