create DATABASE newDB;
create TABLE studentsss(
    id serial primary key,
    name varchar(50),
    dept_id int
)
create table department(
    dept_id int,
    dept_name varchar(50)
)

insert into studentsss(name , dept_id)
values
('Hamna',101),
('Hammad',103),
('Hafsa',104),
('Ahmed',102),
('Zimil',105),
('Zeena',101),
('Zaviar',104),
('AbuBakkar',103),
('Mehmil',103),
('Bareera',102),
('Kainat',105)

select * from studentsss;

insert into department (dept_id , dept_name)
values
(101 , 'Software Engineering'),
(102 , 'Computer Science'),
(103 , 'Civil Engineering'),
(104 , 'Mechanical Engineering'),
(105 , 'Industrial Engineering')

select * from department;

select studentsss.name ,
department.dept_name

from studentsss
inner join department

on studentsss.dept_id = department.dept_id;

select studentsss.name ,
department.dept_name

from studentsss
left join department

on studentsss.dept_id = department.dept_id;

select studentsss.name ,
department.dept_name

from studentsss
right join department

on studentsss.dept_id = department.dept_id;
