# Hackathon_Test


# Bank Account Creation API (Flask + SQLAlchemy + Sql Server)

## Overview
A Flask REST API for bank account creation where customers can register, choose an account type, and open a new account.  
The system automatically generates a unique account number and validates the initial deposit based on account type.

---

## System Design

### Customer Model
Stores customer information.  

| Field | Type | Description |
|-------|------|-------------|
| id | UUID | Unique customer ID | Primary Key
| full_name | String | Customer name |
| email | String | Must be unique |
| phone_number | String | Must be unique |
| address | String | Optional |
| created_at | DateTime | Auto timestamp |

---

### Account Model
Linked to the customer through a foreign key.  

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary key |
| account_number | String(12) | Auto-generated |
| account_type | String | Savings / Current / Fixed Deposit |
| balance | Float | Initial balance |
| status | String | Active / Pending |
| created_at | DateTime | Auto timestamp |
| customer_id | UUID | Linked to Customer |

---

## Planned API Endpoints

### POST/api/AccountCreation
Creates a new Account for the existing customer

**Input:**
json
{
  "customer_id": "uuid-1234",
  "account_type": "Savings",
  "initial_deposit": 1500
}

### POST/api/customers
Creates a new customer. 

**Input:**
json
{
  "full_name": "John Doe",
  "email": "john@example.com",
  "phone_number": "9876543210",
  "address": "Bengaluru, India"
}
