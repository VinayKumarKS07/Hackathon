import pytest
import json
import uuid

class TestCustomerResource:
    def test_create_customer_success(self, client):
        """Test successful customer creation via API"""
        customer_data = {
            "full_name": "Jane Smith",
            "email": "jane@example.com", 
            "phone_number": "9123456780",
            "address": "Mumbai, India"
        }
        
        response = client.post('/customers', 
                             data=json.dumps(customer_data),
                             content_type='application/json')
        
        assert response.status_code == 201
        data = json.loads(response.data)
        
        assert data['message'] == 'Customer registered successfully'
        assert data['customer']['full_name'] == "Jane Smith"
        assert 'id' in data['customer']

    def test_get_customer_by_id_success(self, client):
        """Test getting customer by ID via API"""
        # First create a customer
        customer_data = {
            "full_name": "Test User",
            "email": "test@example.com",
            "phone_number": "9111111111", 
            "address": "Test City"
        }
        
        create_response = client.post('/customers', 
                                    data=json.dumps(customer_data),
                                    content_type='application/json')
        created_customer = json.loads(create_response.data)['customer']
        
        # Now get the customer by ID - use your actual route
        response = client.get(f'/customers/id/{created_customer["id"]}')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['customer']['email'] == "test@example.com"

    def test_get_customer_by_email_success(self, client):
        """Test getting customer by email via API"""
        # First create a customer
        customer_data = {
            "full_name": "Email Test User",
            "email": "emailtest@example.com",
            "phone_number": "9222222222",
            "address": "Test City"
        }
        
        client.post('/customers', 
                   data=json.dumps(customer_data),
                   content_type='application/json')
        
        # Now get the customer by email - use your actual route
        response = client.get('/customers/email/emailtest@example.com')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['customer']['email'] == "emailtest@example.com"

    def test_get_customer_not_found(self, client):
        """Test getting non-existent customer via API"""
        response = client.get(f'/customers/id/{str(uuid.uuid4())}')
        
        assert response.status_code == 404
        data = json.loads(response.data)
        assert 'error' in data