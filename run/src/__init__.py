#!/usr/bin/env python3

from flask import Flask

from .controller.public import controller as public_controller


app = Flask(__name__)

app.register_blueprint(public_controller)
