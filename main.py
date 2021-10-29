from flask import Flask
from db import db_binder
from apis import insurances
import os



db_binder.initDB()

app = Flask(__name__)
app.config["DEBUG"] = True
insurances.api.init_app(app)
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
