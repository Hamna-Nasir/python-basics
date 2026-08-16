CREATE DATABASE StudentManagement123;

create table studentTable(
    id serial primary key,
    name varchar(50),
    age int,
    department varchar(50),
    cgpa float
)

insert into studentTable (name , age ,department ,cgpa )
values
('Hamna',21,'Software Engineering',3.86),
('Ali',22,'Software Engineering',3.2),
('Ahmed',20,'Software Engineering',3.5),
('Fatima',22,'Civil Engineering',2.9),
('Sarim',21,'Biomdeical Engineering',3.1),
('Sidra',23,'Electronic Engineering',3.0),
('Sundus',21,'Software Engineering',3.6),
('Hadiya',20,'Mechanical Engineering',2.7),
('Hammad',19,'Industrial Engineering',3.2),
('Areeba',23,'Textile Engineering',2.5)

select * from studentTable;

select count(*)
from studenttable;

insert into studentTable (name , age ,department ,cgpa )
values
('Hameed' , 23 , 'Computer Science' , 3.2),
('Hurma' , 20 , 'Computer Science' , 2.8)

select sum(age)
from studentTable;

select avg(cgpa) as avg_cgpa
from studentTable;

select max(cgpa)
from studentTable;

select min(cgpa)
from studenttable;

SELECT DISTINCT department
FROM studentTable;

SELECT *
FROM studentTable
ORDER BY cgpa;

SELECT *
FROM studenttable
ORDER BY cgpa DESC;

SELECT department,
COUNT(*)
FROM studentTable
GROUP BY department;

SELECT department,
MAX(cgpa)
FROM studentTable
GROUP BY department;

SELECT department,
AVG(cgpa)
FROM studentTable
GROUP BY department
HAVING AVG(cgpa) > 3.6;

SELECT department,
COUNT(*)
FROM studentTable
WHERE age > 20
GROUP BY department;

SELECT department,
COUNT(*) AS Total_Students,
AVG(cgpa) AS Average_CGPA
FROM studentTable
GROUP BY department
HAVING COUNT(*) >= 1
ORDER BY Average_CGPA DESC;

SELECT *
FROM studentTable
WHERE cgpa IS NOT NULL;

