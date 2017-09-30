from app import settings
from app.router import router
from app.logger import LOGGER


def start_server():
    LOGGER.debug('Starting application in {mode} mode...'.format(
        mode='debug' if settings.DEBUG else 'production'
    ))
    router.run(host=settings.STANDALONE_HOST, port=settings.STANDALONE_PORT, debug=settings.DEBUG, threaded=True)


if __name__ == '__main__':
    start_server()
