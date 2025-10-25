from models.AccountModel import Account
from repositories.AccountRepository import AccountRepository
import random

class AccountService:
    def __init__(self):
        self.repo = AccountRepository()

    def create_account(self, data):
        account_number = str(random.randint(100000000000, 999999999999))

        account = Account(
            account_number=account_number,
            account_type=data["account_type"],
            balance=data["initial_deposit"],
            customer_id=data["customer_id"],
            status="Active"
        )
        return self.repo.create_account(account)
    
    def get_by_account_number(self , account_number):
        return self.repo.get_by_account_number(account_number=account_number);