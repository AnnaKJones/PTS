#!/usr/bin/python3
import sql
import mysql.connector
from mysql.connector import Error
 
 
def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='pts',
                                       user='root',
                                       password='root7749')
        if conn.is_connected():
            print('Connected to MySQL database')
 
    except Error as e:
        print(e)
 
    finally:
        conn.close()
 
    
def insert_name(fname, lname):
    query = "INSERT INTO user(fname,lname) " \
            "VALUES(%s,%s)"
    args = (fname, lname)
 
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='pts',
                                       user='root',
                                       password='root7749')
        if conn.is_connected():
            print('Connected to MySQL database')
 
        cursor = conn.cursor()
        cursor.execute(query, args)
 
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()

def display_name():
    query = "SELECT * FROM user;"
    #args = (fname, lname)
 
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='pts',
                                       user='root',
                                       password='root7749')
        if conn.is_connected():
            print('Connected to MySQL database')
 
        cursor = conn.cursor()
        cursor.execute(query)
 
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()

def insert_course(name, code):
    query = "INSERT INTO course(name,code) " \
            "VALUES(%s,%s)"
    args = (name, code)
 
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='pts',
                                       user='root',
                                       password='root7749')
        if conn.is_connected():
            print('Connected to MySQL database')
 
        cursor = conn.cursor()
        cursor.execute(query, args)
 
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()

def delete_course(code):
    query = "DELETE FROM course WHERE code = ' ' "
    args = code
 
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='pts',
                                       user='root',
                                       password='root7749')
        if conn.is_connected():
            print('Connected to MySQL database')
 
        cursor = conn.cursor()
        cursor.execute(query, args)
 
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()

def insert_session(course, time, place,tutor, student, status):
    query = "INSERT INTO session(course, time, place,tutor, student, status) " \
            "VALUES(%s,%s, %s,%s, %s,%s)"
    args = (course, time, place,tutor, student,status)
 
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='pts',
                                       user='root',
                                       password='root7749')
        if conn.is_connected():
            print('Connected to MySQL database')
 
        cursor = conn.cursor()
        cursor.execute(query, args)
 
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
