import sqlite3
import time

connection = None
cursor = None


def connect(path):
    global connection, cursor

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA foreign_keys=ON; ')
    connection.commit()
    return


def drop_tables():
    global connection, cursor

    drop_course = "DROP TABLE IF EXISTS course; "
    drop_student = "DROP TABLE IF EXISTS student; "
    drop_enroll = "DROP TABLE IF EXISTS enroll; "

    cursor.execute(drop_enroll)
    cursor.execute(drop_student)
    cursor.execute(drop_course)


def define_tables():
    global connection, cursor

    course_query = '''
                        CREATE TABLE course (
                                    course_id INTEGER,
                                    title TEXT,
                                    seats_available INTEGER,
                                    PRIMARY KEY (course_id)
                                    );
                    '''

    student_query = '''
                        CREATE TABLE student (
                                    student_id INTEGER,
                                    name TEXT,
                                    PRIMARY KEY (student_id)
                                    );
                    '''

    enroll_query = '''
                    CREATE TABLE enroll (
                                student_id INTEGER,
                                course_id INTEGER,
                                enroll_date DATE,
                                PRIMARY KEY (student_id, course_id),
                                FOREIGN KEY(student_id) REFERENCES student(student_id),
                                FOREIGN KEY(course_id) REFERENCES course(course_id)
                                );
                '''

    cursor.execute(course_query)
    cursor.execute(student_query)
    cursor.execute(enroll_query)
    connection.commit()

    return


def insert_data():
    global connection, cursor

    insert_courses = '''
                        INSERT INTO course(course_id, title, seats_available) VALUES
                            (1, 'CMPUT 291', 200),
                            (2, 'CMPUT 391', 100),
                            (3, 'CMPUT 101', 300);
                    '''

    insert_students = '''
                            INSERT INTO student(student_id, name) VALUES
                                    (1509106, 'Jeff'),
                                    (1409106, 'Alex'),
                                    (1609106, 'Mike');
                            '''

    cursor.execute(insert_courses)
    cursor.execute(insert_students)
    connection.commit()
    return


def enroll(student_id, course_id):
    global connection, cursor

    current_date = time.strftime("%Y-%m-%d %H:%M:%S")

    """
    	Check that there is a spot in the course for this student.
    """
    crs_id = (course_id,)
    cursor.execute('select seats_availabe from course where course_id=?;', crs_id)
    seats_available = cursor.fetchone()

    """ 
        Register the student in the course.
    """
    if seats_available > 0:
        date = (student_id, course_id, current_date)
        cursor.execute('insert into enroll values (?,?,?);', data)
        cursor.execute('update course set seats_available = seats_available - 1 where course_id=?;', crs_id)

    """
    	Update the seats_available in the course table. (decrement)
    """
    
    connection.commit()
    return


def main():
    global connection, cursor

    path = "./register.db"
    connect(path)
    drop_tables()
    define_tables()
    insert_data()

    #### your part ####
    # register all students in all courses.
    cursor.execute('select * from course;')
    all_courses = cursor.fetchall()

    cursor.execute('select * from student;')
    all_students = cursor.fetchall()

    for every_course in all_courses:
        for every_student in all_students:
            enroll(every_student[0], every_course[0])
    
    print('Printing all enrolled students:')
    print(cursor.execute('select * from enroll;'))
    print(cursor.fetchall())

    connection.commit()
    connection.close()
    return


if __name__ == "__main__":
    main()
