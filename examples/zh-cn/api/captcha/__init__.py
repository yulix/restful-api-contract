from flask import Blueprint

captcha_api = Blueprint('captcha_api', __name__, url_prefix='/api/captcha')

from .captcha import *
