from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from db import db

class Account(db.Model):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    account_number = Column(String(12), unique=True, nullable=False)
    account_type = Column(String(20), nullable=False)
    balance = Column(Float, nullable=False)
    status = Column(String(20), default="Active")
    created_at = Column(DateTime, default=datetime.utcnow)
    customer_id = Column("customer_id", db.ForeignKey("customers.id"))