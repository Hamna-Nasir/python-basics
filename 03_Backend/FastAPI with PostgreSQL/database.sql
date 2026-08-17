create DATABASE managementSystem;

select current_database();

CREATE TABLE students(
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(100),
    cgpa DECIMAL(3,2)
);

INSERT INTO students VALUES
(101,'Hamna',21,'Software Engineering',3.90),
(102,'Ali',22,'Computer Science',3.50),
(103,'Sara',20,'Information Technology',3.80);

select * from students;