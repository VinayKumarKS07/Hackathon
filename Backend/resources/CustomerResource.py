from flask import request
from flask_restful import Resource
from services.CustomerService import CustomerService

class CustomerResource(Resource):
    def __init__(self):
        self.customer_service = CustomerService()

    def post(self):

        try:
            data = request.get_json()

            # required_fields = ['full_name', 'email', 'phone_number']
            # for field in required_fields:
            #     if field not in data:
            #         return {'error': f'Missing required field: {field}'}, 400
            
  
            customer = self.customer_service.register_customer(data)
            
            return {
                'message': 'Customer registered successfully',
                'customer': {
                    'id': str(customer.id),  # Convert UUID to string for JSON
                    'full_name': customer.full_name,
                    'email': customer.email,
                    'phone_number': customer.phone_number,
                    'address': customer.address,
                    'created_at': customer.created_at.isoformat()
                }
            }, 201
            
        except Exception as e:
            return {'error': str(e)}, 400

    def get(self, customer_id=None,email=None):
        
        try:
            if customer_id:
                customer = self.customer_service.get_customer(customer_id)
                return {
                    'customer': {
                        'id': str(customer.id),  # Convert UUID to string
                        'full_name': customer.full_name,
                        'email': customer.email,
                        'phone_number': customer.phone_number,
                        'address': customer.address,
                        'created_at': customer.created_at.isoformat()
                    }
                }, 200
            elif email:
                
                # email = request.args.get('email')
               
                customer = self.customer_service.get_customer_by_email(email)
                if not customer:
                    return {'error': 'Email parameter is required'}, 400
                
                return {
                    'customer': {
                        'id': str(customer.id),  # Convert UUID to string
                        'full_name': customer.full_name,
                        'email': customer.email,
                        'phone_number': customer.phone_number,
                        'address': customer.address,
                        'created_at': customer.created_at.isoformat()
                    }
                }, 200
                
        except Exception as e:
            return {'error': str(e)}, 404