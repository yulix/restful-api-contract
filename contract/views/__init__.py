from flask import render_template
from contract.api.config import LANG
from .. import app


from mock import mockview

app.register_blueprint(mockview)


@app.route('/')
def index():
    f = '{}/index.html'.format(LANG)
    return render_template(f, doc=app.doc)
