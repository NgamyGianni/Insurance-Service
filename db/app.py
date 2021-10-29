import flask
from flask import jsonify, request
import json
from db_binder import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/v1/insurances', methods=['GET'])
def homePage():
	insurances = allInsurances() # get insurances
	return insurances

@app.route('/api/v1/insurances/id/<id>', methods=['GET'])
def pageById(id):
	insurancesbyId = searchInsuranceByKey(1)
	return insurancesbyId

@app.route('/api/v1/insurances/deals/<id>', methods=['GET'])
def pageByDealId(id):
	return id

@app.route('/api/v1/insurances/facilities/<id>', methods=['GET'])
def pageByFacilityId(id):
	return id

@app.route('/api/v1/insurances/add', methods=['POST'])
def pageAddInsurance():
	return request.form.get('test')

app.run()