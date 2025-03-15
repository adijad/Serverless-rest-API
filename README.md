# AWS Lambda Functions for MySQL-based Web Application  

## Overview  
This repository contains a set of **AWS Lambda functions** developed for the **backend of a database-driven web application**. These Lambda functions serve as the backend for a set of **REST APIs** that interact with a **MySQL database** hosted on **AWS RDS**.  

This is an **extension of the bookstore project**, designed to enhance scalability and serverless computing by leveraging AWS **Lambda, API Gateway, and RDS**.  

---

## Deployment Architecture  
![image](deployment-architecture.png)  

The Lambda functions are deployed using **AWS Lambda** and are invoked through **Amazon API Gateway**. These functions interact with an **AWS RDS (MySQL) instance** and return data in **JSON format**.  

- **Serverless Architecture** – Reduces infrastructure management overhead.  
- **Scalable & Cost-Efficient** – AWS Lambda auto-scales based on API demand.  
- **Secure API Access** – IAM roles and policies ensure restricted access to Lambda and RDS.  

---

## API Endpoints  
The following API endpoints are exposed via **AWS Lambda** and **Amazon API Gateway**:  

| **Endpoint**            | **Description** |
|-------------------------|----------------|
| **`/getAllCategory`**   | Fetch all categories from the database. |
| **`/getCategoryName`**  | Given a category ID, fetch its name. |
| **`/getCategoryId`**    | Fetch the category ID for a given category name. |
| **`/addCategory`**      | Add a new category to the database. |
| **`/getAllBook`**       | Fetch all books from the database. |
| **`/getBookById`**      | Fetch book details given the book ID. |
| **`/getBookByCategoryId`** | Fetch books belonging to a given category ID. |
| **`/getBookByCategoryName`** | Fetch books belonging to a given category name. |
| **`/getRandomBook`**    | Fetch 5 random books from the database. |
| **`/addBook`**          | Add a new book to the database. |

All API responses are returned in JSON format** for easy integration with the frontend.  

---

## Database Schema (AWS RDS - MySQL)  
The database schema and sample data for this project are provided in:  
- **schema.sql** – Defines the table structure.  
- **data.sql** – Contains sample records for initial testing.  

- **Database hosted on AWS RDS (MySQL)**  
- **Secure access via IAM roles and VPC networking**  
- **Scalable to support large datasets**  

---

## AWS Lambda Layers & Dependencies  
To optimize deployment and improve efficiency, common dependencies for Lambda functions are **deployed as AWS Lambda Layers**.  

- **Shared libraries and modules** are bundled into layers.  
- **Reduces package size** for each Lambda function, improving execution performance.  
-  **Ensures efficient reusability** across multiple functions.  

---

## Security & IAM Roles  
- **IAM Policies & Roles** – Defined to grant minimum necessary permissions.  
- **API Gateway Authorization** – Proper authorization controls for invoking Lambda functions.  
- **Lambda Access to RDS** – IAM roles allow secure database interactions.  
- **AWS CloudWatch Logging** – All Lambda functions log execution details for monitoring and debugging.  

---
