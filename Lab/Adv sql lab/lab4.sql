-- lab_assignment1.sql

-- Assignment 1

-- Task 1: Retrieve information about students born after June 16, 2009.
SELECT * FROM Student WHERE DateOfBirth > '2009-06-16';

-- Task 2: Retrieve records of students whose first names start with either 'A' or 'J'.
SELECT * FROM Student WHERE FirstName LIKE 'A%' OR FirstName LIKE 'J%';

-- Task 3: Retrieve records of students whose first name is not 'Alice' and whose email addresses contain the domain '@example.com'.
SELECT * FROM Student WHERE FirstName != 'Alice' AND Email LIKE '%@example.com%';

-- Assignment 2

-- Task 1: Create a table Person with PersonID as PRIMARY KEY.
CREATE TABLE Person (
    PersonID INT PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Age INT
);

-- Task 2: Create a table Employee with emp_id as PRIMARY KEY.
CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT
);

-- Task 3: Insert data into Person table.
INSERT INTO Person (PersonID, FirstName, LastName, Age) VALUES (1, 'John', 'Doe', 28);
INSERT INTO Person (PersonID, FirstName, LastName, Age) VALUES (2, 'Jane', 'Smith', 22);

-- Task 4: Insert data into Employee table.
INSERT INTO Employee (emp_id, first_name, last_name, age) VALUES (101, 'Michael', 'Brown', 32);
INSERT INTO Employee (emp_id, first_name, last_name, age) VALUES (102, 'Emily', 'White', 26);

-- Task 5: Create Union of two tables.
SELECT FirstName, LastName, Age FROM Person
UNION
SELECT first_name, last_name, age FROM Employee;

-- lab_assignment2.sql

-- Lab 1: Retrieve student enrollment details using inner join.
SELECT Student.StudentID, Student.FirstName, Student.LastName, Enrollment.EnrollmentID, Enrollment.CourseID 
FROM Student
INNER JOIN Enrollment ON Student.StudentID = Enrollment.StudentID;
