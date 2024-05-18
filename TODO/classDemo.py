# class Person:
#     def __init__(self,pPay,pCourse,pName):
#         self.pay=pPay
#         self.course=pCourse
#         self.name=pName
#     def __str__(self):
#         return "Name= %s, Course= %s,payment=%d" % (self.name, self.course, self.payment)
    
class Payee:
    def __init__(self, position,payment,salary):
        self.position=position
        self.payment=payment
        self.salary=salary
        
    def __str__(self):
        return 'The position is %s, payment is %d,salary is %d' % (self.position, self.payment, self.salary)
    def calculatePay(self):
        pay=int(input("Enter the amount you receive"))
        hours=int(input("Enter the number of hours you work per day"))
        salary=(pay*hours*30)*12
        print("Yearly Pay is : ", salary)
        
        
                 