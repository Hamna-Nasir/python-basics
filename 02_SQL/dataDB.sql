create DATABASE dataDB;

create table employes(
    id serial primary key ,
    emp_name varchar(50),
    salary int ,
    year_of_Experience int,
    dept_id int
);
insert into employes(emp_name , salary , year_of_experience , dept_id)
values
('Hamna', 100000 , 1 , 101),
('Hammad', 150000 , 3 , 101),
('Ahmed', 10000 , 0 , 102),
('Aqeeb', 200000 , 3 , 103),
('Mehfooz', 100000 , 1 , 101),
('Aiman', 130000 , 2 , 102),
('Mehrooz', 300000 , 4 , 101),
('Zareen', 100000 , 2 , 103),
('Zimil', 150000 , 3 , 102);



SELECT current_database();