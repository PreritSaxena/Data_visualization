-- Lab 1: BankAccount Table

-- Task 1: Insert data into the BankAccount table
INSERT INTO BankAccount (account_id, account_holder_name, account_balance) 
VALUES (101, 'Alice Johnson', 45000),
       (102, 'Bob Smith', 25000),
       (103, 'Charlie Brown', 30000),
       (104, 'David Williams', 60000),
       (105, 'Eva Green', 70000);

-- Task 2: Retrieve the account_holder_name and account_balance of all account holders
SELECT account_holder_name, account_balance 
FROM BankAccount;

-- Task 3: Retrieve the account_holder_name and account_balance where the account_balance is more than 30,000
SELECT account_holder_name, account_balance 
FROM BankAccount 
WHERE account_balance > 30000;

-- Task 4: Update the account_balance of the account holder whose ID is 101
UPDATE BankAccount 
SET account_balance = 50000 
WHERE account_id = 101;

-- Lab 1: Student Table - Ordering by Last Name

-- Task: Retrieve students and display results in ascending order based on their last names
SELECT * 
FROM Student 
ORDER BY LastName ASC;

-- Lab 2: Student Table - Count by Gender

-- Task: Count the number of students based on their gender
SELECT Gender, COUNT(*) AS GenderCount 
FROM Student 
GROUP BY Gender;

-- Lab 1: Employee Table - Adding Columns and Retrieving Data

-- Task: Add Salary and Department columns to the Employee table
ALTER TABLE Employee
ADD Salary DECIMAL(10, 2),
ADD Department VARCHAR(50);

-- Task: Insert data into the Employee table including Salary and Department
INSERT INTO Employee (emp_id, first_name, last_name, age, email, Salary, Department) 
VALUES (201, 'John', 'Doe', 35, 'john.doe@example.com', 55000, 'IT'),
       (202, 'Jane', 'Smith', 28, 'jane.smith@example.com', 48000, 'HR'),
       (203, 'Emily', 'Jones', 42, 'emily.jones@example.com', 62000, 'IT'),
       (204, 'Michael', 'Brown', 31, 'michael.brown@example.com', 47000, 'Finance'),
       (205, 'Sarah', 'Davis', 38, 'sarah.davis@example.com', 59000, 'Marketing');

-- Task: Retrieve all employees in the IT department with a salary greater than 50,000
SELECT * 
FROM Employee 
WHERE Salary > 50000 AND Department = 'IT';
