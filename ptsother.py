class user(object):
    """A class representing a user"""
    def __init__(self,n,a,c):
        self.fname = n
        self.age = a
        self.code = c
    def get_fname(self):
        return self.fname
    def set_fname(self):
        self.fname = name
    def __repr__(self):
        return (self.fname +"\n"+ str(self.age)+"\n"+self.code)
class tutor(user):
    """A class extending user, representing tutor"""
    def __init__(self,n,a,c,t="tutor"):
        super(tutor, self).__init__(n,a,c)
        self.Type = t
    def __repr__(self):
        return (self.fname+"\n"+str(self.age)+"\ntc"+self.code+"\n"+self.Type)
class student(user):
    """A class extending user, representing tutor"""
    def __init__(self,n,a,c,t="student"):
        user.__init__(self,n,a,c)
        self.Type = t           
    def __repr__(self):
        return (self.fname+"\n"+str(self.age)+"\nsc"+self.code+"\n"+self.Type)
class course:
    def __init__(self,title):
        self.title = title
    def __repr__(self):
        return (self.title)    
class createsession(tutor,user):     
    def __init__(self,date,place="UWI"):
        super(createsession, self).__init__(n="",a,c,t="tutor")
        self.date = date
        self.place = place
    def get_date(self):
        return self.date
    def set_date(self):
        self.date = date
    def __repr__(self):
        return (self.date+"\n"+self.place)
class picksession(student):
    def __init__(self,place="UWI"):
        self.place = place
 
tutor1 = tutor("mark small",22,"001")
tutor2 = tutor("ren batts",21,"002")
student1 = student("will breks", 19,"003")
student2 = student("ben smith",18,"004")
course1 = course("Physics of the Human Body")
course2 = course("Web Development II")
session1 = createsession("feb12")
