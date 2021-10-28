import flask
from flask import jsonify
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

a = {"name": "ok"}

@app.route('/', methods=['GET'])
def homePage():
    return a

@app.route('/<idi>', methods=['GET'])
def pageById(idi):
    return idi

app.run()