create database shop

use shop

CREATE TABLE tb_user(
id INT PRIMARY KEY identity(1,1) not null,
username VARCHAR(32) not null,
PASSWORD VARCHAR(32) not null,
NAME VARCHAR(32),
telephone VARCHAR(11)
)