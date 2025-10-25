import pytest
import json

class TestAccountResource:
    def test_get_account_by_number_success(self, client):
        
        customer_data = {
            "full_name": "Account Get Test",
            "email": "accountget@example.com",
            "phone_number": "9555555555",
            "address": "Test City"
        }
        
        customer_response = client.post('/customers',
                                      data=json.dumps(customer_data),
                                      content_type='application/json')
        customer_id = json.loads(customer_response.data)['customer']['id']
        
        account_data = {
            "account_type": "Savings",
            "initial_deposit": 3000.0,
            "customer_id": customer_id
        }
        
        create_response = client.post('/api/accountcreation',
                                    data=json.dumps(account_data),
                                    content_type='application/json')
        account_number = json.loads(create_response.data)['account']['account_number']
        
        response = client.get(f'/accounts/{account_number}')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['account']['account_number'] == account_number

    def test_create_account_success(self, client):
       
        customer_data = {
            "full_name": "Account API Test",
            "email": "accountapi@example.com",
            "phone_number": "9444444444",
            "address": "Test City"
        }
        
        customer_response = client.post('/customers',
                                      data=json.dumps(customer_data),
                                      content_type='application/json')
        customer_id = json.loads(customer_response.data)['customer']['id']

        account_data = {
            "account_type": "Savings",
            "initial_deposit": 5000.0,
            "customer_id": customer_id
        }
        
        response = client.post('/api/accountcreation',
                             data=json.dumps(account_data),
                             content_type='application/json')
        
        assert response.status_code == 201
        data = json.loads(response.data)
        
        assert data['message'] == 'Account created successfully'
        assert data['account']['account_type'] == "Savings"
        assert data['account']['balance'] == 5000.0
        assert data['account']['customer_id'] == customer_id