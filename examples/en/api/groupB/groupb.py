# -*- coding: utf-8 -*-
"""
    API specification for Group B
    ~~~~~~~~~~~~~~

    Implements the API contract for Group B.

    :copyright: (c) 2016 by Yu Jiang.
    :license: BSD, see LICENSE for more details.
"""

from flask import jsonify
from . import groupb_api
from contract.core.docme import docme
from contract.core.ctx import *
from contract.core.datatype import *


class Item(Model):
    name = String('name of an item')
    id = Interger('id of an item', 1)


class Items(Model):
    items = List('A list of items', Item())


class PermissonDeny(Model):
    err = String('Permisson denied')


class CtxListItems(CtxEndpoint):
    """The object is used in the context of listing items request.
    """

    title = 'List items'
    # parameters

    # responses
    res200 = Response(code=200, description='List of items')
    res200.content = Items()

    res404 = Response(code=401, description='Permisson denied')
    res404.content = PermissonDeny()


@groupb_api.route('/items', methods=['GET'])
@docme(CtxListItems(groupb_api))
def list_items(id):
    return jsonify({"msg": "DIY responses here!"})



class Success(Model):
    msg = String('Success', defaultvalue='OK')


class CtxCreateItem(CtxEndpoint):
    """The object used for the CreateItem URL.
    """

    title = 'Create a new item'
    # parameters
    name = BodyVariable(description='New name')
    detail = BodyVariable(description='New details')

    # responses
    res200 = Response(code=200, description='Data of an item')
    res200.content = Success()

    res404 = Response(code=404, description='Not found')
    res404.content = PermissonDeny()


@groupb_api.route('/items', methods=['POST'])
@docme(CtxCreateItem(groupb_api))
def create_item(id):
    return jsonify({"msg": "DIY responses here!"})
