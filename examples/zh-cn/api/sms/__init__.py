from flask import Blueprint

sms_api = Blueprint('sms_api', __name__, url_prefix='/api/sms')


from .sms import *

