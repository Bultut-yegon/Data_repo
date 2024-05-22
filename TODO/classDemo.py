# class Person:
#     def __init__(self,pPay,pCourse,pName):
#         self.pay=pPay
#         self.course=pCourse
#         self.name=pName
#     def __str__(self):
#         return "Name= %s, Course= %s,payment=%d" % (self.name, self.course, self.payment)
    
class Payee:
    # init method initializes the variables
    def __init__(self, position,payment,salary):
        self._position=position
        self.payment=payment
        self.salary=salary
        
        # str method returns a human readable string
    def __str__(self):
        return 'The position is %s, payment is %d,salary is %d' % (self._position, self.payment, self.salary)
    #calculate pay is a method that calculates the net salary of a certain member
    def calculatePay(self):
        pay=int(input("Enter the amount you receive"))
        hours=int(input("Enter the number of hours you work per day"))
        salary=(pay*hours*30)*12
        print("Yearly Pay is : ", salary)
        
        #we can access objects instance variables using a dot operator
        # example payee.payment, payee.position, payee.salary
        
    '''Properties of class and methods. It allows us to check on the 
    changes we want to make before executing them'''
    
    # Lets dive into properties now

# we use underscore in front of the variable name. Let's look at the self.position variable and change it
    @property # a decorator function
    def position(self):
        print('Getter method')
        return self._position
    
    @position.setter # decorator function. It has parameter value that is assigned to the position variable
    def position(self, value):
        if value == "manager" or value == "clerk":
            self._position = value
        else:
            return "Not available position"

    
    
        
        
        
                 