# -*- coding: utf-8 -*-

import json

class DataType(object):
    def __init__(self, description, defaultvalue=None):
        self.description = description
        self.defaultvalue = defaultvalue


class Interger(DataType):
    pass


class Float(DataType):
    pass


class String(DataType):
    pass


class DateTime(DataType):
    pass


class List(DataType):
    def __init__(self, description, element=None):
        self.description = description
        self._element = element



class MetaMODEL(type):
    def __new__(cls, name, bases, attrs):
        inst = type.__new__(cls, name, bases, attrs)
        fields = []
        for attrname, attrobj in attrs.items():
            if isinstance(attrobj, DataType):
                attrobj.fieldname = attrname
                fields.append(attrobj)
        inst.fields = fields
        return inst


class Model(object):
    __metaclass__ = MetaMODEL

    def to_doc(self):
        doc = {}
        for field in self.fields:
            doc[field.fieldname] = field.description
        return json.dumps(doc, indent=True)

    def to_json(self):
        values = {}
        for field in self.fields:
            values[field.fieldname] = field.defaultvalue
        return values
