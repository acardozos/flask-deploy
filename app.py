#-------------------------------------------------------------------------------
# Name:        app.py
# Purpose:
#
# Author:      Adolfo J. Cardozo S. - acai.engineering.ia@gmail.com
#
# Created:     08/07/2021
# Copyright:   (c) Adolfo J. Cardozo S. 2021 [ACAI Engineering ia]
# Licence:     MIT
#-------------------------------------------------------------------------------
import logging
import os
import config
from api import api

from flask import Flask

from models import db


logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler()])

logger = logging.getLogger()


def create_app():
    logger.info(f'Starting app in {config.APP_ENV} environment')
    app = Flask(__name__)
    app.config.from_object('config')
    api.init_app(app)
    # initialize SQLAlchemy
    db.init_app(app)

    # define landing page
    @app.route('/')
    def hello_world():
        return 'Welcome to the Flask API RESTFUL deployed in Heroku.'

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
