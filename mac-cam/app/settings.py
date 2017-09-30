"""
Override any setting in local_settings.py.
"""

# Camera source
# Specify an integer like 0, 1, 2 for the id of the camera connecting to.
# Alternatively you may specify a string here pointing to a video file.
SOURCE = 0

# Auth
AUTH_USERNAME = 'user'
AUTH_PASSWORD = 'change-this-to-super-secret'

# Do not turn this on in production mode.
DEBUG = False

# Host and port listened to in standalone mode.
STANDALONE_HOST = '0.0.0.0'
STANDALONE_PORT = 5000

# Logging
LOG_LEVEL = 'DEBUG'
LOG_NAME = 'mac-cam.log'
LOG_MAX_BYTES = 1000000
LOG_BACKUP_COUNT = 9

# Whether returning rate-limiting headers.
# See details in https://flask-limiter.readthedocs.io/en/stable/#ratelimit-headers.
LIMIT_RETURN_HEADER = True

# Global limit.
# See details in https://flask-limiter.readthedocs.io/en/stable/#rate-limit-string-notation.
LIMIT_DEFAULT = [
    '2 per second',
    '1000 per hour'
]

try:
    from local_settings import *
except:
    pass
