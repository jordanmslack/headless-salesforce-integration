from decouple import config
from flask import request, Blueprint, jsonify
import json
from simple_salesforce import Salesforce, SalesforceMalformedRequest


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/v1/case/feedback', methods=['POST'])
def case_feedback():

    """
    """

    sf = Salesforce(
        username=config('USERNAME'),
        password=config('PASSWORD'),
        security_token=config('SALESFORCE_TOKEN')
    )

    data = json.loads(request.data.decode())

    if request.method == 'POST' and not data['_bot-catch']:

        try:

            case = sf.Case.update(
                data.get('case_id', ''), {
                    'Rating__c': data.get('rating', ''),
                    'Feedback__c': data.get('feedback', '')
                }
            )

            response = f"""Case feedback has been successfully added to case: {case['id']}"""

            return jsonify(
                response=response,
                status=201,
                mimetype='application/json'
            )

        except SalesforceMalformedRequest as e:

            return jsonify(
                response=e,
                status=403,
                mimetype='application/json'
            )

    elif data['_bot-catch']:
        response = f"""It would appear that this was an attempt to complete a form via bot: {data['_bot-catch']}"""

        return jsonify(
            response=response,
            status=418,
            mimetype='application/json'
        )


@api.route('/v1/lead', methods=['POST'])
def post_lead():

    """
    """

    sf = Salesforce(
        username=config('USERNAME'),
        password=config('PASSWORD'),
        security_token=config('SALESFORCE_TOKEN')
    )

    data = json.loads(request.data.decode())

    if request.method == 'POST' and not data['_bot-catch']:

        try:

            lead = sf.Lead.create(
                {
                    'FirstName': data.get('first_name', ''),
                    'LastName': data.get('last_name', ''),
                    'Email': data.get('email', ''),
                    'Company': data.get('email', ''),
                    'LeadSource': 'Website',
                }
            )

            return jsonify(
                response=f"Lead successfully created: {lead['id']}",
                status=201,
                mimetype='application/json'
            )

        except SalesforceMalformedRequest as e:

            return jsonify(
                response=e,
                status=403,
                mimetype='application/json'
            )

    elif data['_bot-catch']:

        response = f"""It would appear that this was an attempt to complete a form via bot: {data['_bot-catch']}"""
        return jsonify(
            response=response,
            status=418,
            mimetype='application/json'
        )
