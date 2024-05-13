class Person:
    def __init__(self,pPay,pCourse,pName):
        self.pay=pPay
        self.course=pCourse
        self.name=pName
    def __str__(self):
        return "Name= %s, Course= %s,payment=%d" % (self.name, self.course, self.payment)
       
        