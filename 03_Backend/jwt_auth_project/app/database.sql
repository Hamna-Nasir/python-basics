CREATE DATABASE jwt_auth_db;
select * from users;
UPDATE users
SET role='admin'
WHERE username='hamna';