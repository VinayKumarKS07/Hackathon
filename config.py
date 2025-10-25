import os

class Config:
    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc://@localhost/BankDB?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
                                                                        
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "supersecretkey")