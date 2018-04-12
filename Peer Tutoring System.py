import random

class User:
    '''Represents a system user'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized User: {})'.format(self.name))

    def toString(self):
        '''Dispay of a user'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Tutor(User):
    '''Represents a tutor'''
    def __init__(self, name, age):
        SchoolMember.__init__(self, name, age)
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)


class Student(User):
    '''Represents a student.'''
    def __init__(self, name, age):
        SchoolMember.__init__(self, name, age)
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)


class Course:
    '''Represents a system user'''
    def __init__(self, name, avSession):
        self.name = name
        self.avSession = avSession
        print('(Initialized Course: {})'.format(self.name))


class Session:
    '''Represents a system user'''
    def __init__(self, course, time, place, tutor, student):
        self.course = course
        self.time = time
        self.place = place
        self.tutor = tutor
        self.student = student
        self.sessCode = random.randint(0, 100) #Note: change so that code is in form AA0000
        print('(Initialized Session: {})'.format(self.sessCode))

    def toString(self):
        print('Course Name:"{}" Time:"{}" Code:"{}"'.format(self.course,
                                self.time, self.sessCode), end=" ")
