#!/usr/bin/python3
import random
import sql
import Connector



class User:
    '''Represents a system user'''
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.name= self.fname +" "+ self.lname
        self.bio = ''
        self.strike=Strike(self)
        Connector.insert_name(self.fname,self.lname)
        print('(Initialized User: {})'.format(self.name))
        
    messages=["has cancelled session", "has requested session", "has approved your request for"
              , "has denied your request for"]

    def setBio(self,bio):
        self.bio=bio

    def toString(self):
        '''Dispay of a user'''
        print('Name:"{}" Bio:"{}"'.format(self.name, self.bio), end=" ")

    def cancelSession(session):
        session.status="Available"
        return message[1]

    


class Tutor(User):
    '''Represents a tutor'''
    def __init__(self, fname, lname):
        User.__init__(self, fname, lname)
        print('(Initialized Teacher: {})'.format(self.name))

    def toString(self):
        User.toString(self)

    def setBio(self,bio):
        User.setBio(self)

    def approveSession(m):
        m= ('{}', messages[2], '{}'.format(self.name, session))
        session.status="Upcoming"
        return m

    def declineSession(m):
        m= ('{}', messages[3], '{}'.format(self.name, session))
        return m

    def addSession(self, course, time, place,tutor, student):
        return TimetableBridge.addSession(self, course, time, place,tutor, student)

    def cancelSession(session):
        User.cancel(session)
        

class Student(User):
    '''Represents a student.'''
    def __init__(self, fname, lname):
        User.__init__(self, fname, lname)
        print('(Initialized Student: {})'.format(self.name))

    def toString(self):
        User.toString(self)

    def setBio(self,bio):
        User.setBio(self)

    def requestSession(session):
        m=('{} has requested {}'.format(self.name, session))

    def cancelSession(session):
        session.student=''
        User.cancel(session)


class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        Connector.insert_course(self.name,self.code)
        print('(Initialized Course: {})'.format(self.name))

    def toString(self):
        print('Name:"{}" Code:"{}"'.format(self.name, self.code), end=" ")


class Session:
    def __init__(self, course, time, place, tutor, student):
        self.course = course
        self.time = time
        self.place = place
        self.tutor = tutor
        self.student = student
        self.sessCode = random.randint(0, 100) #Note: change so that code is in form AA0000
        self.status= "Available"
        Connector.insert_course(self.course,self.time, self.place, self.tutor, self.student, self.status)
        print('(Initialized Session: {})'.format(self.sessCode))

    def toString(self):
        print('Course Name:"{}" Time:"{}" Code:"{}"'.format(self.course,
                                self.time, self.sessCode), end=" ")

class SessionReview:
    def __init__(self, review):
        self.review=review

class Strike:
    def __init__(self):
        self.number=0
        print('(Initialized Strike: {})'.format(self.number))

    def toString(self):
        print('Strike number: "{}"'.format(self.number))

class Timetable:
    def addSession(self, course, time, place,tutor, student):
        newSess=Session(course, time, place,tutor, student)
        return newSess.toString()

class Schedule:
    def addSession(self, course, time, place,tutor, student):
        newSess=Session(course, time, place,tutor, student)
        return newSess.toString()
            
class TimetableBridge:
    def __init__(self, ttCode, ttType):
        self.ttCode = ttCode
        self.ttType=ttType
        self.content=[]
        print('(Initialized Timetable: {})'.format(self.ttCode))

    def addSession(self, course, time, place,tutor, student):
        newSess=[self.ttType.createSession(self,course, time, place,tutor, student)]
        #self.content.append(newSess)
        #print(self.content)

class AdminUser():
    def addCourse(name, code):
        Course(name, code)

    def delCourse(code):
        Connector.delete_course(code)

