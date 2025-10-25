from flask import request
from flask_restful import Resource
from services.AccountService import AccountService

class AccountResource(Resource):
    def __init__(self):
        self.account_service = AccountService()

    def post(self):
        try:
            data = request.get_json()
            required_fields = ['account_type', 'initial_deposit', 'customer_id']
            for field in required_fields:
                if field not in data:
                    return {'error': f'Missing required field: {field}'}, 400
            if(data['account_type'] not in ['Savings', 'Checking']):
                return {'error': 'Invalid account type. Must be Savings or Checking'}, 400
            if(data['initial_deposit']<1500 and data['account_type'] =='savings'):
                return {'error': 'Minimum initial deposit for Savings account is 1500'},400
            if(data['initial_deposit']<5000 and data['account_type']=='checking'):
                return {'error': 'Minimum initial deposit for Savings account is 1500'}, 
            
            if data['initial_deposit'] < 0:
                return {'error': 'Initial deposit cannot be negative'}, 400
            
            account = self.account_service.create_account(data)
            
            return {
                'message': 'Account created successfully',
                'account': {
                    'id': account.id,
                    'account_number': account.account_number,
                    'account_type': account.account_type,
                    'balance': account.balance,
                    'status': account.status,
                    'customer_id': str(account.customer_id),
                    'created_at': account.created_at.isoformat()
                }
            }, 201
            
        except Exception as e:
            return {'error': str(e)}, 400

    def get(self, account_number=None):
       
        try:
            if account_number:
                account = self.account_service.get_by_account_number(account_number)
                if not account:
                    return {'error': 'Account not found'}, 404
                    
                return {
                    'account': {
                        'id': account.id,
                        'account_number': account.account_number,
                        'account_type': account.account_type,
                        'balance': account.balance,
                        'status': account.status,
                        'customer_id': str(account.customer_id),
                        'created_at': account.created_at.isoformat()
                    }
                }, 200
            else:
                return {'error': 'Account number is required'}, 400
                
        except Exception as e:
            return {'error': str(e)}, 500