from models.AccountModel import Account
from db import db

class AccountRepository:
    def create_account(self, account):
        db.session.add(account)
        db.session.commit()
        return account
    
    def get_by_account_number(self, account_number):
        return Account.query.filter_by(account_number=account_number).first();