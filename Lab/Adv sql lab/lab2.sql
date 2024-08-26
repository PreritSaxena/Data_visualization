-- lab_assignment1.sql

-- Lab 1: Insert 5 records into each table and retrieve data from all tables

-- Insert records into Student table
INSERT INTO Student (FirstName, LastName, DateOfBirth, Gender, Email, Phone) VALUES
('John', 'Doe', '2000-01-15', 'Male', 'john.doe@example.com', '1234567890'),
('Jane', 'Smith', '2001-02-20', 'Female', 'jane.smith@example.com', '1234567891'),
('Alice', 'Johnson', '1999-03-25', 'Female', 'alice.johnson@example.com', '1234567892'),
('Bob', 'Brown', '2002-04-30', 'Male', 'bob.brown@example.com', '1234567893'),
('Charlie', 'Davis', '2000-05-10', 'Male', 'charlie.davis@example.com', '1234567894');

-- Insert records into Course table
INSERT INTO Course (CourseTitle, Credits) VALUES
('Mathematics', 4),
('Physics', 3),
('Chemistry', 4),
('Biology', 3),
('Computer Science', 5);

-- Insert records into Instructor table
INSERT INTO Instructor (FirstName, LastName, Email) VALUES
('Roger', 'White', 'roger.white@example.com'),
('Alice', 'Green', 'alice.green@example.com'),
('John', 'Black', 'john.black@example.com'),
('Emma', 'Blue', 'emma.blue@example.com'),
('Henry', 'Gray', 'henry.gray@example.com');

-- Insert records into Enrollment table
INSERT INTO Enrollment (EnrollmentDate, StudentID, CourseID, InstructorID) VALUES
('2024-01-10', 1, 1, 1),
('2024-01-15', 2, 2, 2),
('2024-01-20', 3, 3, 3),
('2024-01-25', 4, 4, 4),
('2024-01-30', 5, 5, 5);

-- Insert records into Score table
INSERT INTO Score (CourseID, StudentID, DateOfExam, CreditObtained) VALUES
(1, 1, '2024-05-15', 3),
(2, 2, '2024-05-16', 3),
(3, 3, '2024-05-17', 4),
(4, 4, '2024-05-18', 2),
(5, 5, '2024-05-19', 4);

-- Insert records into Feedback table
INSERT INTO Feedback (StudentID, Date, InstructorName, Feedback) VALUES
(1, '2024-02-10', 'Roger White', 'Excellent teaching'),
(2, '2024-02-12', 'Alice Green', 'Very helpful'),
(3, '2024-02-15', 'John Black', 'Needs improvement'),
(4, '2024-02-18', 'Emma Blue', 'Great course'),
(5, '2024-02-20', 'Henry Gray', 'Well explained');

-- Retrieve data from all tables
SELECT * FROM Student;
SELECT * FROM Course;
SELECT * FROM Instructor;
SELECT * FROM Enrollment;
SELECT * FROM Score;
SELECT * FROM Feedback;

-- lab_assignment2.sql

-- Task 1: Insert Data
-- Insert records into Employee table
INSERT INTO Employee (first_name, last_name, age, email) VALUES
('Michael', 'Smith', 45, 'michael.smith@example.com'),
('Sarah', 'Johnson', 32, 'sarah.johnson@example.com'),
('James', 'Williams', 28, 'james.williams@example.com'),
('Linda', 'Jones', 40, 'linda.jones@example.com'),
('Robert', 'Brown', 50, 'robert.brown@example.com');

-- Task 2: Retrieving Data
-- Retrieve first_name and last_name of all employees
SELECT first_name, last_name FROM Employee;

-- Task 3: Filtering Data
-- Retrieve first_name, last_name, and age of employees older than 30 years
SELECT first_name, last_name, age FROM Employee WHERE age > 30;

-- Task 4: Updating Data
-- Increase the age of employees by 1 year for all employees older than 25
UPDATE Employee SET age = age + 1 WHERE age > 25;
