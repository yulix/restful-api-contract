# -*- coding: utf-8 -*-
"""
    API specification for Group A
    ~~~~~~~~~~~~~~

    Implements the API contract for Group A.

    :copyright: (c) 2016 by Yu Jiang.
    :license: BSD, see LICENSE for more details.
"""

from flask import jsonify
from . import groupa_api
from contract.core.docme import docme
from contract.core.ctx import *
from contract.core.datatype import *


class Item(Model):
    name = String('Name of item', defaultvalue='valueOfname')
    detail = String('Details of item', defaultvalue='valueOfdetails')


class ItemNotFound(Model):
    msg = String('Error', defaultvalue='Not found')


class CtxGetItem(CtxEndpoint):
    """The object used for the GetItem URL.
    """

    title = 'Read data of an item'
    # parameters
    id = PathVariable(description='ID of an item')

    # responses
    res200 = Response(code=200, description='Data of an item')
    res200.content = Item()

    res404 = Response(code=404, description='Not found')
    res404.content = ItemNotFound()


@groupa_api.route('/item/<id>', methods=['GET'])
@docme(CtxGetItem(groupa_api))
def get_item_data_by_id(id):
    return jsonify({"msg": "DIY responses here!"})



class Success(Model):
    msg = String('Success', defaultvalue='OK')


class CtxUpdateItem(CtxEndpoint):
    """The object used for the UpdateItem URL.
    """

    title = 'Update data of an item'
    # parameters
    id = PathVariable(description='ID of an item')
    name = BodyVariable(description='New name')
    detail = BodyVariable(description='New details')

    # responses
    res200 = Response(code=200, description='Data of an item')
    res200.content = Success()

    res404 = Response(code=404, description='Not found')
    res404.content = ItemNotFound()


@groupa_api.route('/item/<id>', methods=['PUT'])
@docme(CtxUpdateItem(groupa_api))
def update_item_data(id):
    return jsonify({"msg": "DIY responses here!"})
