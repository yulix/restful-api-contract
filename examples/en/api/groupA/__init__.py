from flask import Blueprint


groupa_api = Blueprint('groupa_api', __name__, url_prefix='/groupA')

from .groupa import *
