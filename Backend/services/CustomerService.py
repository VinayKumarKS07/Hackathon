from models.CustomerModel import Customer
from repositories.CustomerRepository import CustomerRepository

class CustomerService:
    def __init__(self):
        self.repo = CustomerRepository()

    def register_customer(self, data):
        existing = self.repo.get_by_email(data["email"])
        if existing:
            raise Exception("Customer already exists")

        customer = Customer(
            full_name=data["full_name"],
            email=data["email"],
            phone_number=data["phone_number"],
            address=data.get("address", "")
        )
        return self.repo.add_customer(customer)
    
    def get_customer(self, customer_id):
        customer = self.repo.get_by_id(customer_id)
        if not customer:
            raise Exception("Customer not found")
        return customer
    
    def get_customer_by_email(self, email):
        customer = self.repo.get_by_email(email)
        if not customer:
            raise Exception("Customer not found")
        return customer