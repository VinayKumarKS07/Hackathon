import pytest
from services.AccountService import AccountService
from services.CustomerService import CustomerService

class TestAccountService:
    def test_create_account_success(self, client):
        """Test successful account creation"""
        with client.application.app_context():
            customer_service = CustomerService()
            customer_data = {
                "full_name": "Account Test",
                "email": "account@example.com",
                "phone_number": "9333333333",
                "address": "Test City"
            }
            customer = customer_service.register_customer(customer_data)
            account_service = AccountService()
            account_data = {
                "account_type": "Savings",
                "initial_deposit": 1000.0,
                "customer_id": str(customer.id)  # Convert to string
            }

            account = account_service.create_account(account_data)

            assert account is not None
            assert account.account_type == "Savings"
            assert account.balance == 1000.0
            assert str(account.customer_id) == str(customer.id)

    def test_get_account_by_number_success(self, client):
        with client.application.app_context():
            customer_service = CustomerService()
            customer_data = {
                "full_name": "Account Test",
                "email": "account@example.com",
                "phone_number": "9333333333",
                "address": "Test City"
            }
            customer = customer_service.register_customer(customer_data)

            account_service = AccountService()
            account_data = {
                "account_type": "Savings",
                "initial_deposit": 1000.0,
                "customer_id": str(customer.id)  # Convert to string
            }
            account = account_service.create_account(account_data)

            retrieved_account = account_service.get_by_account_number(account.account_number)

            assert retrieved_account is not None
            assert retrieved_account.account_number == account.account_number
            assert str(retrieved_account.customer_id) == str(customer.id)