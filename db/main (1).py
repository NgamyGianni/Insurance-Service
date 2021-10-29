from flask import Flask
import db_binder
import insurance
import os

#db_binder.initDB()

app = Flask(__name__)
app.config["DEBUG"] = True
insurance.api.init_app(app)
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
