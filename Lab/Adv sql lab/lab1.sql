CREATE DATABASE StudentManagementSystem;
USE StudentManagementSystem;

CREATE TABLE Student (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DateOfBirth DATE,
    Gender ENUM('Male', 'Female', 'Other'),
    Email VARCHAR(100),
    Phone VARCHAR(15)
);

CREATE TABLE Course (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,
    CourseTitle VARCHAR(100),
    Credits INT
);

CREATE TABLE Instructor (
    InstructorID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100)
);

CREATE TABLE Enrollment (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY,
    EnrollmentDate DATE,
    StudentID INT,
    CourseID INT,
    InstructorID INT,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
    FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID)
);

CREATE TABLE Score (
    ScoreID INT AUTO_INCREMENT PRIMARY KEY,
    CourseID INT,
    StudentID INT,
    DateOfExam DATE,
    CreditObtained INT,
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
);

CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY,
    StudentID INT,
    Date DATE,
    InstructorName VARCHAR(100),
    Feedback TEXT,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
);
