from flask import request, jsonify, Response
from flask_restplus import Api, Resource, fields
import json
import requests
from db import db_binder

api = Api(
    version="1.0",
    title="insurances API",
    description="Api of MicroService Insurances"
)
name_space = api.namespace('insurances', description='insurances APIs')
resource_fields = api.model('Resource', {
})

resource_fields1 = api.inherit('Resource1', resource_fields, {
    'code_insurance': fields.String,
    'insurance_name': fields.String,
    'insurance_actived': fields.Boolean,

})

resource_fields2 = api.inherit('Resource2', resource_fields, {
    'insuranceContractCode': fields.String,
    'insurance_code' : fields.String,
    'dealCode': fields.String,
    'facilityCode': fields.String,
    'amount': fields.Float,
    'currency': fields.String
})



@api.route('/api/v1/insurances')
class insurances(Resource):
    @api.response(200, 'Success')
    def get(self):
        """Returns list of insurances."""
        result_dic = db_binder.allInsurances()
        result = json.dumps(result_dic)
        return Response(result, status=200, mimetype='application/json')

    @api.response(200, 'Success')
    @api.response(400, 'Validation Error')
    @api.expect(resource_fields1)
    def post(self):

        content = request.json
        print (content)
        code = content['code_insurance']
        name = content['insurance_name']
        actived = content['insurance_actived']


        response = db_binder.createInsurance(code, name,actived)
        if response == False:
            return {'error': 'wrong request'}, 400
        result = json.dumps(response)
        return jsonify(result)


@api.route('/api/v1/insurances/<code>')
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
            return "Flag changed with success"
        return jsonify(result)

@api.route('/api/v1/deals/<deal_code>/insurance-contracts')
@api.doc(params={'deal_code': 'insurance-contract code'})
class insurance_Contract(Resource):
    @api.response(200, 'Success')
    def get(self,deal_code):
        """Returns list of insurances."""
        result = db_binder.searchInsuranceContractByDeal(deal_code)
        statusCode = 200
        if result == -1:
            return {'error': "contract don't exist"}, 400
        return Response(json.dumps(result), status=statusCode, mimetype='application/json')
        

       
@api.route('/api/v1/deals/{deal-code}/facilities/{facility-code}/insurance-contracts')
class insurance_Contract2(Resource):
    
    @api.response(200, 'Success')
    @api.response(400, 'Validation Error')
    @api.expect(resource_fields2)
    def post(self):

        content = request.json
        print (content)
        contractKey = content['insuranceContractCode']
        codeAssurance = content['insurance_code']
        codeDeal = content['dealCode']
        codeFacility = content['facilityCode']
        amount = content['amount']
        currency = content['currency']

        response = db_binder.createInsuranceContract(contractKey,codeAssurance,codeDeal,codeFacility,amount,currency)
        if response == False:
            return {'error': 'wrong request'}, 400
        result = json.dumps(response)
        return jsonify(result)
