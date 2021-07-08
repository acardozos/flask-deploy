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
from celery import Celery
import config


def make_celery():
    celery = Celery(__name__, brocker=config.CELERY_BROKER)
    celery.conf.update(config.as_dict())
    return celery


celery = make_celery()

