-- lab_assignment1.sql

-- Lab 1

-- Task 1: RIGHT OUTER JOIN query to retrieve data for students and their enrollments, even if some students are not enrolled in any courses.
SELECT Student.StudentID, Student.FirstName, Student.LastName, Enrollment.EnrollmentID, Enrollment.CourseID
FROM Enrollment
RIGHT JOIN Student ON Enrollment.StudentID = Student.StudentID;

-- Task 2: LEFT JOIN query to retrieve data for students and their enrollments, even if some enrollments do not have corresponding students.
SELECT Student.StudentID, Student.FirstName, Student.LastName, Enrollment.EnrollmentID, Enrollment.CourseID
FROM Student
LEFT JOIN Enrollment ON Student.StudentID = Enrollment.StudentID;

-- Lab 2

-- Task 1: FULL OUTER JOIN query to retrieve details of students and their enrollments, including students without enrollments and enrollments without corresponding students.
SELECT Student.StudentID, Student.FirstName, Student.LastName, Enrollment.EnrollmentID, Enrollment.CourseID
FROM Student
FULL OUTER JOIN Enrollment ON Student.StudentID = Enrollment.StudentID;

-- Task 2: NATURAL JOIN query to retrieve details of students and their enrollments where StudentID matches in both tables.
SELECT Student.StudentID, Student.FirstName, Student.LastName, Enrollment.EnrollmentID, Enrollment.CourseID
FROM Student
NATURAL JOIN Enrollment;
