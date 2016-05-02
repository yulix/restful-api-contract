from flask import Blueprint
from flask import render_template, jsonify, request
from .. import app
from contract.api.config import LANG


mockview = Blueprint('mockview', __name__, url_prefix='/mock')


@mockview.route('/')
def index():
    f = '{}/mock.html'.format(LANG)
    return render_template(f, doc=app.doc)


@mockview.route('/response', methods=['PUT'])
def set_response():
    rspcode = int(request.form['rspcode'])
    path = request.form['path']
    ctx = app.doc.get_ctx(path)
    if ctx:
        print("OK")
        ctx.set_current_rsp(rspcode)
        return jsonify({'msg': 'OK'})
    else:
        print("Error")
        return jsonify({'msg': 'Error'})
