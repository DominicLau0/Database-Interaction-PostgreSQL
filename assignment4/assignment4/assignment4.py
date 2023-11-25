import psycopg2

def getAllStudents():
    #Retrieve all records from student table
    try:
        cur.execute('SELECT * FROM students')
    
        for data in cur.fetchall():
            print(data)
    except Exception as error:
        print(error)
        conn.rollback()
     
def addStudent(first_name, last_name, email, enrollment_date):
    #Allow enrollment date to be null if not specified.
    if enrollment_date == "":
        enrollment_date = None

    try:
        #Insert data into student table
        insert_string = 'INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)'
        value = (first_name, last_name, email, enrollment_date)
    
        cur.execute(insert_string, value)
        conn.commit()
    except Exception as error:
        print(error)
        conn.rollback()
    
def updateStudentEmail(student_id, new_email):
    #Update data from student table
    try:
        update_string = 'UPDATE students SET email = %s WHERE student_id = %s'

        cur.execute(update_string, (new_email, student_id))
        conn.commit()
    except Exception as error:
        print(error)
        conn.rollback()

def deleteStudent(student_id):
    #Delete data from student table
    try:
        delete_string = 'DELETE FROM students WHERE student_id = %s'
    
        cur.execute(delete_string, (student_id,))
        conn.commit()
    except Exception as error:
        print(error)
        conn.rollback()
    
def createTable():
    #Create the table if not done so in Postgre
    create_table_string = '''CREATE TABLE students (
	                            student_id SERIAL PRIMARY KEY,
	                            first_name TEXT NOT NULL,
	                            last_name TEXT NOT NULL,
	                            email TEXT NOT NULL UNIQUE,
	                            enrollment_date DATE
                            )'''
    cur.execute(create_table_string)
    conn.commit()

try:
    #Connect to the postgres server
    conn = psycopg2.connect(database = 'assignment4',
                            user = 'postgres',
                            host = 'localhost',
                            password = '7982088dom123',
                            port = 5432)

    cur = conn.cursor()
    
    '''
    #Create table and populate data (If not done so in Postgre)
    createTable()
    addStudent("John", "Doe", "john.doe@example.com", "2023-09-01")
    addStudent("Jane", "Smith", "jane.smith@example.com", "2023-09-01")
    addStudent("Jim", "Beam", "jim.beam@example.com", "2023-09-02")
    '''
    
    #Ask users to what they want to do with the database
    while True:
        print("Select the type of operation you want.")
        print("1. Display all records from the students table.")
        print("2. Insert a new student record into the students table.")
        print("3. Update the email address for a student.")
        print("4. Delete the record of student.")
        print ("0. Stop the program.\n")
        
        value = int(input("Enter your selection: "))
        
        if value == 0:
            break
        elif value == 1:
            getAllStudents() 
            
        elif value == 2:
            first_name = input("Enter the student's first name: ")
            last_name = input("Enter the student's last name: ")
            email = input ("Enter the student's email: ")
            enrollment_date = input("Enter the student's enrollment_date: ")
            
            addStudent(first_name, last_name, email, enrollment_date)
            
        elif value == 3:
            student_id_update = input("Enter the student's id: ")
            new_email = input("Enter the student's new email: ")
            
            updateStudentEmail(student_id_update, new_email)
            
        elif value == 4:
            student_id_delete = int(input("Enter the student's id: "))
            
            deleteStudent(student_id_delete)
            
        else:
            print("Your input is invalid.")
            
        print()
    
    #Close the connection
    cur.close()
    conn.close()
    
except Exception as error:
    print(error) 