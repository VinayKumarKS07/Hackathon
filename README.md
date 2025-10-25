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
  "customer_id": "ad7d4fda-6606-4aaa-bdf4-16bf096fec56",
  "account_type": "Checking",
  "initial_deposit": 1700
}

**output**
json
{
    "message": "Account created successfully",
    "account": {
        "id": 7,
        "account_number": "280399659126",
        "account_type": "Checking",
        "balance": 1700.0,
        "status": "Active",
        "customer_id": "ad7d4fda-6606-4aaa-bdf4-16bf096fec56",
        "created_at": "2025-10-25T09:57:15.520000"
    }
}

### GET/api/Account/{account_number}

input :(280399659126)account_number 

output:
{
 "account": {
        "id": 7,
        "account_number": "280399659126",
        "account_type": "Checking",
        "balance": 1700.0,
        "status": "Active",
        "customer_id": "ad7d4fda-6606-4aaa-bdf4-16bf096fec56",
        "created_at": "2025-10-25T09:57:15.520000"
    }
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

**output**
{
    "message":"Customer Created Successfully",
    "customer": {
        "id": "58eba8cd-5fe4-443d-b9b5-225109494d5e",
        "full_name": "John Doe",
        "email": "john@example.com",
        "phone_number": "9876543210",
        "address": "Bengaluru, India",
        "created_at": "2025-10-25T08:49:09.190000"
    }

    
### GET/api/customers/{Customer_Id}
input:58eba8cd-5fe4-443d-b9b5-225109494d5e(Customer_id)
output:
{ "customer": {
        "id": "58eba8cd-5fe4-443d-b9b5-225109494d5e",
        "full_name": "John Doe",
        "email": "john@example.com",
        "phone_number": "9876543210",
        "address": "Bengaluru, India",
        "created_at": "2025-10-25T08:49:09.190000"
    }
}


