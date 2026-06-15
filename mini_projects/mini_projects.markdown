## What's in this chapter?:

So this chapter consists of programs that work as a whole and demonstrate the use of various python concepts.

1. bank_account.py - A simple bank account management system
2. ATM-machine.py - A simple ATM system
3. shopping_inventory.py - A simple shopping inventory system
4. shopping_users.py - Registration Logic
5. Shopping_sellers.py - Program for sellers to manage their inventory
6. Shopping_users.py - Program for users to buy products

## Concepts Used:

1. bank_account.py:

- Classes & Objects
- String Manipulation
- Date & Time Handling
- Random Generation
- Control Flow
- User Input Validation
- File Handling & Data Persistence

2. ATM-machine.py:

- Classes & Objects
- Inheritance
- Method overriding 
- Instance Attributes
- Class Relationships
- Time Module
- File Handling & Data Persistence

3. shopping_inventory.py:

- Classes & Objects
- Constructor 
- JSON Reading and Writing
- Abstract Base Classes
- Method Overriding
- Composition
- Encapsulation
- Magic Methods
- Polymorphism
- List Comprehensions
- File Handling & Data Persistence

4. shopping_customers.py:

- Classes & Objects
- Inheritance
- Advanced Data Structures
- Search Algorithms
- Mathematical and Logical Operations
- Exception Handling
- List Methods
- Enumerations
- File Handling & Data Persistence

5. Shopping_sellers.py:

- Classes & Objects
- Inheritance
- Inventory Management
- Data Validation
- Dictionary Operations
- Flag Variables
- User authentication 
- File Handling & Data Persistence

6. Shopping_users.py:

- Classes & Objects
- Inheritance
- Control Flow
- Dictionary Operations
- String Methods
- Data Structures
- File Handling & Data Persistence

## Inheritance Hierarchy:

```
Products (base product class)
    ↑
Items (ABC with abstract method)
    ↑
├── Electronics
├── Stationaries  
├── Textiles
├── Books
└── Grocery

```

## System Flow & Integration:

┌─────────────────┐     ┌─────────────────┐
│  bank_account   │────▶│  acc_database   │
│   (register)    │     │    .json        │
└────────┬────────┘     └────────┬────────┘
         │                       │
         ▼                       ▼
┌─────────────────┐     ┌─────────────────┐
│  shopping_users │     │  ATM-machine    │
│  (role assign)  │     │  (deposit/etc)  │
└────────┬────────┘     └─────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│         Role Check                       │
│    ┌──────────┴──────────┐              │
│    ▼                     ▼              │
│ ┌──────────────┐   ┌──────────────┐     │
│ │   Customer   │   │   Seller     │     │
│ │shopping_customers│ │shopping_sellers │ │
│ └──────┬───────┘   └──────┬───────┘     │
│        │                  │              │
│        ▼                  ▼              │
│ ┌──────────────┐   ┌──────────────┐     │
│ │    Cart      │   │  Inventory   │     │
│ │  Checkout    │   │  Management  │     │
│ │  Tax calc    │   │              │     │
│ └──────────────┘   └──────────────┘     │
└─────────────────────────────────────────┘



## THANK YOU FOR REVIEW! KINDLY REPORT THE LOGICAL ERRORS IF ANY.