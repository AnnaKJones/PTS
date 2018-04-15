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
#def main():
 #  insert_name('Anna','Jones')
 
#if __name__ == '__main__':
 #   insert_name(fname,lname)
