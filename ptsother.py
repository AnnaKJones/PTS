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
class createsession(object):     
    def __init__(self,id,course,time,date,location,tutor,status,place="UWI"):
        self.id = id
        self.course = course
        self.time = time
        self.date = date
        self.location = location
        self.tutor = tutor
        self.place = place
        self.status = status
    def changetime(self, newtime):
        self.time = newtime
        return self.time
    def changedate(self, newdate):
        self.date = newdate
        return self.date
    def changelocation(self, newlocation):
        self.location = newlocation
        return self.location
    def changestatus(self, newstatus):
        self.status = newstatus
        return self.status
    def __repr__(self):
        return (self.id+"\n"+self.date+"\n"+self.place)
class picksession(createsession):
    def __init__(self,id,course,time,date,location,tutor,student,status="Engaged",place="UWI"):
        super(picksession, self).__init__(id,course,time,date,location,tutor,status,place="UWI")
        self.student = student
    def changestatus(self, newstatus):
        self.status = newstatus
        return self.status    
    def __repr__(self):
        return (self.course+"\n"+self.date+"\n"+self.place)
class review(object):
    def __init__(self,id,time,date,name,info):
        self.id = id
        self.time = time
        self.date = date
        self.name = name
        self.info = info
    def __repr__(self):
        return (self.info)
        
tutor1 = tutor("mark small",22,"001")
tutor2 = tutor("ren batts",21,"002")
student1 = student("will breks", 19,"003")
student2 = student("ben smith",18,"004")
course1 = course("Physics of the Human Body")
course2 = course("Web Development II")
session1 = createsession("s001","course1","5pm","feb21","room1","tutor1","Available")
sessionpick1 = picksession("s001","course1","5pm","feb21","room1","tutor1","student1")
review1 = review("r001","12pm","feb22","heron chambers","The session was just wonderful")
