from db import db
from app import app
from models.CustomerModel import Customer
from models.AccountModel import Account


with app.app_context():
    db.create_all()