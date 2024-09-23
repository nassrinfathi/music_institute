create database mft;

create table mft.student_tbl(
    id int primary key auto_increment,
    name varchar(30),
    family varchar(30),
    national_id varchar(10),
    phone varchar(11),
    address varchar(50),
    grade varchar(2)
);