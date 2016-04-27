# -*- coding: utf-8 -*-

from flask import jsonify
from . import captcha_api
from contract.core.docme import docme
from contract.core.ctx import *
import json

class CtxCaptchaReq(CtxEndpoint):
    title = u'获取验证码'
    passthrough = True
    # parameters
    codetype = QueryVariable(description=u'验证类型')
    service = QueryVariable(description=u'服务分类')
    # response
    res200 = ResponseEntity(code=200, description=u'成功，验证码已发送')
    res200.content = {"status": "OK"}
    res401 = ResponseEntity(code=401, description=u'未授权')
    res401.content = {"status": "Error", "msg": "No Permission"}


@captcha_api.route('/code', methods=['GET'])
@docme(CtxCaptchaReq(captcha_api))
def captcha_get_code():
    from flask import request
    return jsonify({'msg': u'Passthrough模式',
                   'input': str(request)})


class CtxCaptchaVerify(CtxEndpoint):
    title = u'校验验证码'
    # parameters
    codetype = QueryVariable(description=u'验证类型')
    service = QueryVariable(description=u'服务分类')
    # response
    res200 = ResponseEntity(code=200, description=u'验证码已发送')
    res200.content = {"name": "geetest", "code": "XYZ"}
    res401 = ResponseEntity(code=401, description=u'未授权')
    res401.content = {"msg": "No Permission"}


@captcha_api.route('/code', methods=['POST'])
@docme(CtxCaptchaVerify(captcha_api))
def captcha_verify_code():
    return jsonify({'msg': 'code sent.'})


class CtxCaptchaList(CtxEndpoint):
    title = u'获取校验方法列表'
    # parameters
    # response
    res200 = ResponseEntity(code=200, description=u'成功')
    x = {'page': u'Number 当前页号',
         'pages': u'Number 总页数',
         'user_list': [{'name': u'String 姓名',
                        'phone': u'String 手机号'}]}

    res200.content = json.dumps(x, indent=True, ensure_ascii=False)
    json.dumps
    res401 = ResponseEntity(code=401, description=u'未授权')
    res401.content = {"msg": "No Permission"}


@captcha_api.route('/services', methods=['GET'])
@docme(CtxCaptchaList(captcha_api))
def captcha_list():
    return jsonify({'msg': 'ok'})
