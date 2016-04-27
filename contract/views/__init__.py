from flask import Blueprint
from .. import app

docview = Blueprint('docview', __name__, url_prefix='/doc')
import index

app.register_blueprint(docview)
