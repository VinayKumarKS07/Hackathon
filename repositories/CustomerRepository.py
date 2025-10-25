from models.CustomerModel import Customer
from db import db

class CustomerRepository:
    def add_customer(self, customer):
        db.session.add(customer)
        db.session.commit()
        return customer

    def get_by_email(self, email):
        return Customer.query.filter_by(email=email).first()

    def get_by_id(self, customer_id):
        return Customer.query.get(customer_id)
