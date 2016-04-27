from .. import app

from .groupA import groupa_api
from .groupB import groupb_api

# Register API buleprint
app.register_blueprint(groupa_api)
app.register_blueprint(groupb_api)
