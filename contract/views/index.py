
from flask import render_template


from . import docview
from .. import app
from contract.api.config import LANG


@docview.route('/')
def docentry():
    pass


@app.route('/')
def index():
    f = '{}/index.html'.format(LANG)
    return render_template(f, doc=app.doc)
