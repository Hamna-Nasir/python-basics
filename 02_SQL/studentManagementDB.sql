CREATE DATABASE studentManagement

create table student(
    id serial primary key,
    name varchar(50),
    age int,
    department varchar(50),
    cgpa float
)

insert into student (name , age ,department ,cgpa )
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

select * from student

create table courses (
    course_id serial primary key,
    course_name varchar(50),
    credit_hours int
)

insert into courses (course_name , credit_hours)
values
('Programming Fundamental' , 2),
('Linear Algebra' , 3),
('OOPS' , 2),
('SQL' , 2),
('DSA' , 2),
('Web Engineering' , 2),
('Fundamental Math' , 3),
('Basic English', 3)

select * from courses 

SELECT name, cgpa
FROM student;

SELECT *
FROM student
WHERE department = 'Software Engineering';