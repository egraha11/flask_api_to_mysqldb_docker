    CREATE DATABASE IF NOT EXISTS Online_Store;
    USE Online_Store;
    CREATE TABLE IF NOT EXISTS orders (
        Order_Id INT PRIMARY KEY,
        Price INT,
        Product_Id INT 
    );