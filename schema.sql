-- database schema

create database student_db;
use student_db;

create table admin(
id int auto_increment primary key,
username varchar(50) not null,
password varchar(100) not null
);

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    roll_no VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    branch VARCHAR(50),
    year INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

create table subjects(
id int auto_increment primary key,
name varchar(100) not null,
max_marks int default 100
);

create table marks(
id int auto_increment primary key,
student_id int,
subject_id int,
marks_obtained int,
UNIQUE KEY unique_student_subject (student_id, subject_id),
foreign key (student_id) references students(id) on delete cascade,
foreign key (subject_id) references subjects(id)
);

insert into admin (username,password) values('admin','admin123');

INSERT INTO subjects (name, max_marks) VALUES
('Mathematics', 100), ('Physics', 100),
('Chemistry', 100), ('English', 100), ('Computer Science', 100);




