from models.AccountModel import Account
from repositories.AccountRepository import AccountRepository
import random
import uuid
class AccountService:
    def __init__(self):
        self.repo = AccountRepository()

     
    def create_account(self, data):
        account_number = str(random.randint(100000000000, 999999999999))

        try:
            # Attempt to convert the string to a UUID object
            customer_uuid =uuid.UUID(data["customer_id"])
        except ValueError:
            # Raise a specific exception if the format is wrong
            raise ValueError("Invalid format for customer_id. It must be a valid UUID string.")

        account = Account(
            account_number=account_number,
            account_type=data["account_type"],
            balance=data["initial_deposit"],
            customer_id=customer_uuid, # Use the validated UUID object
            status="Active"
        )
        return self.repo.create_account(account)
    
    def get_by_account_number(self , account_number):
        return self.repo.get_by_account_number(account_number=account_number);