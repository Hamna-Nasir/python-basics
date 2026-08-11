-- Create a table
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(100)
);

-- Insert data
INSERT INTO students (name, age, department)
VALUES
('Hamna', 21, 'Software Engineering'),
('Ali', 22, 'Computer Science'),
('Sara', 20, 'Artificial Intelligence');

-- View data
SELECT * FROM students;


SELECT name, department
FROM students;

SELECT *
FROM students
ORDER BY age DESC;

SELECT *
FROM students
LIMIT 2;

