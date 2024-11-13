# SQL and MongoDB

This repository provides a collection of examples, exercises, and scripts for working with **SQL** and **MongoDB**. It covers fundamental concepts for both relational databases (SQL) and NoSQL databases (MongoDB), helping users understand how to use these databases for data storage, querying, and management.

The content in this repository includes practical demonstrations of CRUD operations, database design, data normalization, aggregation, indexing, and more. It's a useful resource for anyone looking to strengthen their knowledge of both SQL and MongoDB databases.

## Table of Contents

- [Overview](#Overview)
- [Key Features](#key-features)
- [SQL Examples](#sql-examples)
- [MongoDB Examples](#mongodb-examples)
- [Installation](#installation)

## Overview

This repository demonstrates how to interact with SQL databases (like MySQL, PostgreSQL) and MongoDB. It provides practical examples of querying data, creating databases, tables, and collections, and working with real-world datasets.

Key highlights include:
- SQL examples demonstrating SELECT, INSERT, UPDATE, DELETE queries, and JOINs.
- MongoDB examples for document-based storage, aggregation, and querying using MongoDB's powerful features.
- A comparative look at how both databases handle data operations.

## Key Features

- **SQL Examples**: Learn how to create databases, design schemas, and query relational databases using SQL.
- **MongoDB Examples**: Explore document-based storage with MongoDB, including CRUD operations, aggregation, and indexing.
- **Data Modeling**: Understand the differences between relational and NoSQL data models and how to design schemas for both.
- **Aggregation Framework**: MongoDB-specific features like the aggregation pipeline and map-reduce operations.
- **Normalization and Joins**: SQL-specific operations like data normalization and joining tables across relationships.
- **Data Operations**: Perform common database operations like creating tables, inserting records, and querying datasets.

## SQL Examples

This section provides SQL code examples for various operations in relational databases.

### 1. **Database and Table Creation**
```sql
CREATE DATABASE car_dealership;

USE car_dealership;

CREATE TABLE cars (
    car_id INT PRIMARY KEY,
    make VARCHAR(50),
    model VARCHAR(50),
    year INT,
    price DECIMAL(10, 2)
);
```

### 2. **INSERT Operation**
```sql
INSERT INTO cars (car_id, make, model, year, price)
VALUES (1, 'Toyota', 'Corolla', 2020, 20000.00);
```

### 3. **SELECT Operation**
```sql
SELECT * FROM cars WHERE price > 15000;
```

### 4. **JOIN Operation**
```sql
SELECT customers.name, cars.make, cars.model 
FROM customers
JOIN cars ON customers.car_id = cars.car_id;
```

### 5. **UPDATE Operation**
```sql
UPDATE cars 
SET price = 18000 
WHERE car_id = 1;
```

### 6. **DELETE Operation**
```sql
DELETE FROM cars WHERE car_id = 1;
```

## MongoDB Examples

This section demonstrates MongoDB's operations with a focus on CRUD, aggregation, and indexing.

### 1. **Database and Collection Creation**
```javascript
use car_dealership;

db.createCollection("cars");
```

### 2. **INSERT Operation**
```javascript
db.cars.insert({
    car_id: 1,
    make: "Toyota",
    model: "Corolla",
    year: 2020,
    price: 20000.00
});
```

### 3. **FIND Operation**
```javascript
db.cars.find({ price: { $gt: 15000 } });
```

### 4. **Aggregation Example**
```javascript
db.cars.aggregate([
    { $match: { price: { $gt: 15000 } } },
    { $group: { _id: "$make", avg_price: { $avg: "$price" } } }
]);
```

### 5. **Update Operation**
```javascript
db.cars.updateOne(
    { car_id: 1 },
    { $set: { price: 18000 } }
);
```

### 6. **Delete Operation**
```javascript
db.cars.deleteOne({ car_id: 1 });
```

## Installation

### SQL Setup

For SQL, you'll need a relational database management system (RDBMS) such as MySQL or PostgreSQL. Install one of the following:

- **MySQL**: [Download MySQL](https://dev.mysql.com/downloads/)
- **PostgreSQL**: [Download PostgreSQL](https://www.postgresql.org/download/)

### MongoDB Setup

To work with MongoDB, you'll need to install MongoDB locally or use a cloud-based service like MongoDB Atlas:

- **MongoDB**: [Download MongoDB](https://www.mongodb.com/try/download/community)

Alternatively, if you're using MongoDB Atlas (cloud-based), follow their [getting started guide](https://www.mongodb.com/cloud/atlas).
