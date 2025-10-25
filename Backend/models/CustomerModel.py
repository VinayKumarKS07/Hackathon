from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from db import db
import uuid

class Customer(db.Model):
    __tablename__ = "customers"

    id = Column(UNIQUEIDENTIFIER, primary_key=True, default=lambda: str(uuid.uuid4()))
    full_name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    phone_number = Column(String(15), unique=True, nullable=False)
    address = Column(String(200))
    created_at = Column(DateTime, default=datetime.utcnow)
