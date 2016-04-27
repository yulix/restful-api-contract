from flask import Flask
app = Flask(__name__)

from .core.document import Document
mydoc = Document(app)

# Register document blueprint
import views

# Register User's API blueprint
import api.blueprints

# Prepare online doc
mydoc.parse()
