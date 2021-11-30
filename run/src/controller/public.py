#!/usr/bin/env python3

from flask import Blueprint,request,jsonify

from ..model.api import API


controller = Blueprint('public',__name__)


@controller.route('/providers')
def providers():
    if request.method == 'POST':
        return API().get_providers()


@controller.route('/services')
def services():
    if request.method == 'POST':
        return API().get_services()


@controller.route('/regions')
def regions():
    if request.method == 'POST':
        return API().get_regions()

#######################################################################
@controller.route('/products',methods=['POST'])
def products():
    if request.method == 'POST':
        req = request.get_json()
        res = jsonify(
            API().get_products(
                req.get('provider'),
                req.get('service'),
                req.get('region')
            )
        )
        from pprint import pprint
        pprint(res)
        return res
