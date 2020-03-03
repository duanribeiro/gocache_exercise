import logging
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)

else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
