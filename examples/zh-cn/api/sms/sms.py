# -*- coding: utf-8 -*-

from flask import jsonify
from . import sms_api
from contract.core.docme import docme
from contract.core.ctx import *
import json


class CtxSMSCodeReq(CtxEndpoint):
    title = u'获取短信码'
    # parameters
    phone = QueryVariable(description=u'手机号')
    business = QueryVariable(description=u'业务编码')
    # responses
    res200 = ResponseEntity(code=200, description=u'验证码已发送')
    res200.content = json.dumps(
        {"msg": "OK", "event_id": "1243456789"},
        indent=True)
    res401 = ResponseEntity(code=401, description=u'未授权')
    res401.content = {"msg": "No Permission"}


@sms_api.route('/code', methods=['GET'])
@docme(CtxSMSCodeReq(sms_api))
def require_sms_code():
    return jsonify({'msg': 'sms code sent.'})


class CtxSMSCodeVerify(CtxEndpoint):
    title = u'校验短信码'
    # parameters
    phone = QueryVariable(description=u'手机号')
    code = QueryVariable(description=u'收到的验证码')
    event_id = QueryVariable(description=u'事件号')
    # responses
    res200 = ResponseEntity(code=200, description=u'验证码正确')
    res200.content = {"msg": "OK"}
    res401 = ResponseEntity(code=401, description=u'验证码已失效')
    res401.content = {"msg": "Expired"}


@sms_api.route('/verify', methods=['GET'])
@docme(CtxSMSCodeVerify(sms_api))
def verify_sms_code():
    return jsonify({"msg": "OK"})
