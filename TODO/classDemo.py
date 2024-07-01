from abc import ABC,abstractmethod

class Safaricom(ABC):
    def __init__(self,name,age,mobile_number,county):
        self.__name=name
        self.age=age
        self.__mobile_number=mobile_number
        self.county=county
    def __str__(self):
        return 'Name: %s, Age: %d, Mobile Number: %d, County: %s' % (self.name, self.age, self.__mobile_number, self.county)
    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, value):
        invalid = ['!', '@', '#', '$', '%', '^', '&', '*',
               '(', ')', '_', '+', '-', '=', '[', ']', '{', '}',
               ';', "'", ':', '"', '\\', '|', ',', '.', '<', '>', '/', '?']
        # global invalid
        if value == 0 or value in invalid:
            raise ValueError('Invalid name')
        self.__name = value
    @abstractmethod
    def get_mobile_number(self):
        return self.__mobile_number
    def set_mobile_number(self, value):
        if value < 0:
            raise ValueError('Invalid number')
        self.__mobile_number = value

user=Safaricom('Juma', 21, 1234567890, 'Nairobi')
print(user)

class PremiumSafaricom(Safaricom):
    def __init__(self, name, age, mobile_number, county, package):
        super().__init__(name, age, mobile_number, county)
        self.package = package

    def __str__(self):
        return super().__str__() + ', Package: %s' % self.package
    def get_mobile_number(self):
        # return super().get_mobile_number()
        return self.mobile_number()


class GoldSafaricom(Safaricom):
    def __init__(self, name, age, mobile_number, county, bonus_points):
        super().__init__(name, age, mobile_number, county)
        self.bonus_points = bonus_points

    def __str__(self):
        return super().__str__() + ', Bonus Points: %d' % self.bonus_points
    
    def call(self):
        print('Calling...')
    def text(self):
        print('Texting...')
    def retrieving(self):
        print('Retrieving call...')
        
    def busy(self):
        print('You are busy...')    
            


# Example usage
premium_customer = PremiumSafaricom('John Doe', 25, 1234567890, 'Nairobi', 'Premium Plus')
print(premium_customer)

gold_customer = GoldSafaricom('Jane Smith', 30, 9876543210, 'Mombasa', 5000)
print(gold_customer)

customer=Safaricom('John', 21, 1234567890, 'Nairobi')

print(premium_customer.get_mobile_number())
print(gold_customer.get_mobile_number())    