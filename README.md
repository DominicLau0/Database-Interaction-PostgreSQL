# Database-Interaction-PostgreSQL
## Description
This is a Python application that interacts with the PostgreSQL server for COMP 3005 - Assignment #4.

Video Link: https://www.youtube.com/watch?v=wnkAG4t_Jkc

## Summary
This program allow the user to display all student records, insert a new student record, update a student record, and delete a student record.

This python program uses the `psycopg2` library to communicate with the Postgres server.

<br>

`getAllStudents()`: Retrieves all records from the student table.

`addStudent(first_name, last_name, email, enrollment_date)`: Insert data into the student table.

`updateStudentEmail(student_id, new_email)`: Update student's email from the student table.

`deleteStudent(student_id)`: Delete a student record from the student table.

## Installation guide
First install the [SQL file](https://github.com/DominicLau0/Database-Interaction-PostgreSQL/blob/main/SQL%20file.sql).

Then install the [Python file](https://github.com/DominicLau0/Database-Interaction-PostgreSQL/blob/main/assignment4/assignment4/assignment4.py).

Alternatively you can just download the whole entire folder if you want to open this up with Visual Studio.

<br>

Since I'm using the `psycopg2` library, you have to install the library using this in the terminal:

`pip install psycopg2`

`pip3 install psycopg2`
