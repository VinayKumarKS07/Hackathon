import pytest
import uuid
from services.CustomerService import CustomerService
from models.CustomerModel import Customer
from db import db

class TestCustomerService:
    def test_register_customer_success(self, client):
      
        with client.application.app_context():
            service = CustomerService()
            
            customer_data = {
                "full_name": "John Doe",
                "email": "john@example.com",
                "phone_number": "9876543210",
                "address": "Bengaluru, India"
            }
            
            customer = service.register_customer(customer_data)
            
            assert customer is not None
            assert customer.full_name == "John Doe"
            assert customer.email == "john@example.com"
            assert customer.phone_number == "9876543210"
            assert customer.address == "Bengaluru, India"
            assert customer.id is not None

    def test_register_customer_duplicate_email(self, client):
      
        with client.application.app_context():
            service = CustomerService()
            
            customer_data = {
                "full_name": "John Doe",
                "email": "john@example.com",
                "phone_number": "9876543210",
                "address": "Bengaluru, India"
            }
            
            # First registration should succeed
            service.register_customer(customer_data)
            
            # Second registration with same email should fail
            with pytest.raises(Exception, match="Customer already exists"):
                service.register_customer(customer_data)

    def test_get_customer_by_id_success(self, client):
      
        with client.application.app_context():
            service = CustomerService()
            
            customer_data = {
                "full_name": "John Doe",
                "email": "john@example.com",
                "phone_number": "9876543210",
                "address": "Bengaluru, India"
            }
            
            customer = service.register_customer(customer_data)
            retrieved_customer = service.get_customer(str(customer.id))
            
            assert retrieved_customer.id == customer.id
            assert retrieved_customer.email == customer.email

    def test_get_customer_by_id_not_found(self, client):
        """Test getting non-existent customer by ID"""
        with client.application.app_context():
            service = CustomerService()
            
            with pytest.raises(Exception, match="Customer not found"):
                service.get_customer(str(uuid.uuid4()))

    def test_get_customer_by_email_success(self, client):
        """Test getting customer by email"""
        with client.application.app_context():
            service = CustomerService()
            
            customer_data = {
                "full_name": "John Doe",
                "email": "john@example.com",
                "phone_number": "9876543210",
                "address": "Bengaluru, India"
            }
            
            customer = service.register_customer(customer_data)
            retrieved_customer = service.get_customer_by_email("john@example.com")
            
            assert retrieved_customer.id == customer.id
            assert retrieved_customer.email == customer.email

    def test_get_customer_by_email_not_found(self, client):
        """Test getting non-existent customer by email"""
        with client.application.app_context():
            service = CustomerService()
            
            with pytest.raises(Exception, match="Customer not found"):
                service.get_customer_by_email("nonexistent@example.com")