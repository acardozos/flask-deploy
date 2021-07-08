#-------------------------------------------------------------------------------
# Name:        __init__.py
# Purpose:
#
# Author:      Adolfo J. Cardozo S. - acai.engineering.ia@gmail.com
#
# Created:     08/07/2021
# Copyright:   (c) Adolfo J. Cardozo S. 2021 [ACAI Engineering ia]
# Licence:     MIT
#-------------------------------------------------------------------------------
import uuid
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String())
    email = db.Column(db.String(), unique=True)
