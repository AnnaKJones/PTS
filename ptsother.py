class user(object):
    """A class representing a user"""
    def __init__(self,fname,lname,age,code,bio):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.code = code
        self.bio = bio
        self.Type = ""
    def __repr__(self):
        return (self.fname +"\n"+self.lname+"\n"+str(self.age)+"\n"+self.code)
class tutor(user):
    """A class extending user, representing tutor"""
    def __init__(self,fname,lname,age,code,bio,Type="tutor"):
        super(tutor, self).__init__(fname,lname,age,code,bio)        
    def __repr__(self):
        return (self.fname+"\n"+self.lname+"\n"+str(self.age)+"\ntc"+self.code+"\n"+self.bio+"\n"+self.Type)
class student(user):
    """A class extending user, representing tutor"""
    def __init__(self,fname,lname,age,code,bio,Type="student"):
        user.__init__(self,fname,lname,age,code,bio)                    
    def __repr__(self):
        return (self.fname+"\n"+self.lname+"\n"+str(self.age)+"\nsc"+self.code+"\n"+self.Type)
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
        print self.time
    def changedate(self, newdate):
        self.date = newdate
        print self.date
    def changelocation(self, newlocation):
        self.location = newlocation
        print self.location
    def changestatus(self, newstatus):
        self.status = newstatus
        print self.status
    def __repr__(self):
        return (self.id+"\n"+self.course+"\n"+self.time+"\n"+self.date+"\n"+self.location+"\n"+self.tutor+"\n"+self.status+"\n"+self.place)
class picksession(createsession):
    def __init__(self,id,course,time,date,location,tutor,student,status="Engaged",place="UWI"):
        super(picksession, self).__init__(id,course,time,date,location,tutor,status,place="UWI")
        self.student = student
    def changestatus(self, newstatus):
        self.status = newstatus
        print (self.status)
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
tutor1 = tutor("mark","small",22,"001","I love learnig")
tutor2 = tutor("ren","batts",21,"002","I love learnig")
student1 = student("will","breks", 19,"003","I love learnig")
student2 = student("ben","smith",18,"004","I love learnig")
course1 = course("Physics of the Human Body")
course2 = course("Web Development II")
session1 = createsession("s001","course1","5pm","feb21","room1","tutor1","Available")
sessionpick1 = picksession("s001","course1","5pm","feb21","room1","tutor1","student1")
review1 = review("r001","12pm","feb22","heron chambers","The session was just wonderful")
