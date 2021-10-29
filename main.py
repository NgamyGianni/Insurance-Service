import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from db import db_binder
from apis import insurances
import os



db_binder.initDB()

app = Flask(__name__)
app.config["DEBUG"] = True
insurances.api.init_app(app)
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
