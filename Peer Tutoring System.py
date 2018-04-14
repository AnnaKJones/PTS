import random

class User:
    '''Represents a system user'''
    def __init__(self, name):
        self.name = name
        self.bio = ''
        self.strike=0
        print('(Initialized User: {})'.format(self.name))


    def setBio(self,bio):
        self.bio=bio

    def toString(self):
        '''Dispay of a user'''
        print('Name:"{}" Bio:"{}"'.format(self.name, self.bio), end=" ")


class Tutor(User):
    '''Represents a tutor'''
    def __init__(self, name):
        User.__init__(self, name)
        print('(Initialized Teacher: {})'.format(self.name))

    def toString(self):
        User.toString(self)

    def setBio(self,bio):
        User.setBio(self)

class Student(User):
    '''Represents a student.'''
    def __init__(self, name):
        User.__init__(self, name)
        print('(Initialized Student: {})'.format(self.name))

    def toString(self):
        User.toString(self)

    def setBio(self,bio):
        User.setBio(self)


class Course:
    def __init__(self, name, avSession):
        self.name = name
        self.avSession = avSession
        print('(Initialized Course: {})'.format(self.name))

    def toString(self):
        print('Name:"{}" Sessions Available:"{}"'.format(self.name, self.avSession), end=" ")


class Session:
    def __init__(self, course, time, place, tutor, student):
        self.course = course
        self.time = time
        self.place = place
        self.tutor = tutor
        self.student = student
        self.sessCode = random.randint(0, 100) #Note: change so that code is in form AA0000
        self.status= "Available"
        print('(Initialized Session: {})'.format(self.sessCode))

    def toString(self):
        print('Course Name:"{}" Time:"{}" Code:"{}"'.format(self.course,
                                self.time, self.sessCode), end=" ")

class Strike:
    def __init__(self, number):
        self.number=number
        print('(Initialized Strike: {})'.format(self.number))

    def toString(self):
        print('Strike number: "{}"'.format(self.number))

class Timetable:
        def createSession(self, course, time, place,tutor, student):
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
        self.content.append(newSess)
        print(self.content)


