from flask import request, jsonify, Response
from flask_restplus import Api, Resource, fields
import json
import requests
import db_binder

api = Api(
    version="1.0",
    title="insurance API",
    description="Api of MicroService Insurance"
)
name_space = api.namespace('insurance', description='insurance APIs')
resource_fields = api.model('Resource', {
    'code_isurance': fields.String,
    'insurance_name': fields.String,
    'amount': fields.Integer
})


@api.route('/insurance')
class insurances(Resource):
    @api.response(200, 'Success')
    def get(self):
        """Returns list of insurances."""
        result_dic = db_binder.allInsurances()
        result = json.dumps(result_dic)
        return Response(result, status=200, mimetype='application/json')

    @api.response(200, 'Success')
    @api.response(400, 'Validation Error')
    @api.expect(resource_fields)
    def post(self):

        content = request.json
        code = content['code_insurance']
        name = content['insurance_name']
        insur_amount = content['amount']

        response = db_binder.createInsurance(code, name,isur_amount)
        if response == False:
            return {'error': 'wrong request'}, 400
        result = json.dumps(response)
        return jsonify(result)


@api.route('/insurance/<code>')
@api.doc(params={'code': 'insurance code'})
class insuranceid(Resource):
    @api.response(200, 'Success')
    @api.response(400, 'Insurance does not exist')

    def get(self, code):
        """Returns an insurance."""
        result = db_binder.searchInsuranceByKey(code)
        statusCode = 200
        if result == -1:
            return {'error': "contract don't exist"}, 400
        return Response(json.dumps(result), status=statusCode, mimetype='application/json')

    def put(self,code):
        response = db_binder.updateFlag(code)
        if response == -1:
            return {'error': 'wrong request'}, 400
        result = json.dumps(response)
        if response['change_success'] == 1:
            # respPut = changeContract(code_contract)
            return
        return jsonify(result)


# def changeContract(code):
#     response = requests.put('http://127.0.0.1:8091/api/v1/deals/close/' + code, data={'code': code})
#     return response.status_code