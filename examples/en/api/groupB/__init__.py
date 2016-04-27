from flask import Blueprint


groupb_api = Blueprint('groupb_api', __name__, url_prefix='/groupB')

from .groupb import *
