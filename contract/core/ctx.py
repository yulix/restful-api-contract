# -*- coding: utf-8 -*-


class Variable(object):
    pass


# request variable 请求参数名
# 请求参数种类
# 数据类型
# 说明
# 特性： 可选/必填
class InputArg(Variable):
    def __init__(self, name='', datatype='String', description=''):
        self.name = name
        self.datatype = datatype
        self.description = description


class Response(object):
    def __init__(self, code=200, description='', content=''):
        self.code = code
        self.description = description
        self.content = content


class MetaCTX(type):
    def __new__(cls, name, bases, attrs):
        inst = type.__new__(cls, name, bases, attrs)
        parameters = []
        responses = {}
        for attrname, attrobj in attrs.items():
            if isinstance(attrobj, InputArg):
                attrobj.name = attrname
                parameters.append(attrobj)
            if isinstance(attrobj, Response):
                responses[attrname] = attrobj

        if 'passthrough' not in attrs:
            inst.passthrough = False

        inst.parameters = parameters
        if responses:
            inst.responses = responses
            inst.current_rsp = inst.responses['res200']
        return inst


class CtxEndpoint(object):
    __metaclass__ = MetaCTX

    def __init__(self, blueprint):
        self.blueprint = blueprint

    def make_example(self, endpoint):
        from flask import url_for
        data = {}
        for i in self.parameters:
            if isinstance(i, (PathVariable, QueryVariable)):
                data[i.name] = 'xxx'
        return url_for(endpoint, **data)


# parameters in URL path of HTTP reuests
# example:  http://example.com/user/<int:id>
class PathVariable(InputArg):
    @property
    def location_str(self):
        return 'URL path'


# parameters in query string of HTTP reuests
# example: http://example.com/user/search?name=abc
class QueryVariable(InputArg):
    @property
    def location_str(self):
        return 'Query string'


# parameters in body of HTTP PUT or POST
# mime: application/x-www-form-urlencoded
# example: parameter=value&also=another

class BodyVariable(InputArg):
    @property
    def location_str(self):
        return 'Body'


# parameters in body of HTTP PUT or POST
# mime: multipart/form-data
class FormVariable(InputArg):
    def location_str(self):
        return 'Body'


# HTTP header
class HeaderVariable(InputArg):
    pass


class ResponseModel(object):
    pass


class RequestModel(object):
    pass
