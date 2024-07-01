# def word_count(text):
#     frequency={}
#     # global words,frequency
#     # words=text.split() # split the text
#     # frequency={}
    
    
#     for element in text:
#        if element in frequency:
#             frequency[element]+=1
#        else:
#             frequency[element]=1
#     return frequency
# count=word_count('Missing a lot of tasks')
# print(count)

# def sum_nested_dict(nested_dict):
#     total_sum = 0

#     def recursive_sum(d):
#         nonlocal total_sum
#         for value in d.values():
#             if isinstance(value, dict):
#                 recursive_sum(value)
#             else:
#                 total_sum += value

#     recursive_sum(nested_dict)
#     return total_sum
# nested_dict = {
#     'a': 1,
#     'b': {
#         'c': 2,
#         'd': {
#             'e': 3,
#             'f': 4
#         }
#     },
#     'g': 5
# }

# result = sum_nested_dict(nested_dict)
# print(result)  # Output: 15
# print(nested_dict[1][1][1])

# c=lambda w: w*20
# print(c(10))

# pro=lambda x,y: (x*y)/(x+y)
# print(pro(10,20))

# import time
# timestapper=lambda: time.localtime()

# print(timestapper())

# def get_num(m):
#     return lambda x: x*m

# myfunction=get_num(3)
# myfunction1=get_num(4)
# print(myfunction(20))
# print(myfunction1(22))

# Using lambda with map
numbers = [1, 2, 3, 4,39,20,56]
squares = map(lambda x: x**3, numbers)# x is the variable used to represent numbers 
print(list(squares))  # Output: [1, 4, 9, 16]
names=['jack','jill','john','jane']
uppercase=list(map(lambda s: s.upper(),names))
print(uppercase)
capitalized=tuple(map(lambda d: d.capitalize(),names))
print(capitalized)

# Using lambda with filter
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]
fruits=['apple','banana','cherry','orange','kiwi','melon','mango','pineapple','papaya','grapes','watermelon']
filtered=tuple(filter(lambda fruit: fruit.startswith('m'), fruits))
print(filtered)

# Using lambda with reduce
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24
maximum_num=reduce(lambda a,b: a if a>b else b, numbers)
print(maximum_num)

# Using lambda with sorted
numbers = [5, 2, 8, 1, 9]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)  # Output: [1, 2, 5, 8, 9]
people_choice=[
    ('Victor', 9),
    ('Jack', 20),
    ('Jill', 21),
    ('John', 22),
    ('Jane', 23)
    ]
age=sorted(people_choice, key=lambda w: w[1])
print(age)
stock=[{'name': 'Product B', 'price': 5.99},
 {'name': 'Product D', 'price': 8.99},
 {'name': 'Product A', 'price': 10.99},
 {'name': 'Product C', 'price': 15.99}]
stock_sort=sorted(stock, key=lambda value: value['price'])
print(stock_sort)

#classes and objects
# class Instructor:
#     def __init__(self,name,youtube_channel_name,age,country,rating):
#         self.name=name
#         self.__youtube_channel_name=youtube_channel_name
#         self.age=age
#         self.country=country
#         self.rating=rating
#     def _str__(self):
#         return f'Name: {self.name}, Youtube Channel Name: {self.__youtube_channel_name}, Age: {self.age}, Country: {self.country}, Rating:{self.rating} '
#     def display(self):
#         return (f'Name: {self.name}, Youtube Channel Name: {self.__youtube_channel_name}, Age: {self.age}, Country: {self.country}, Rating:{self.rating} ')
            
#     # pass
# instructor_1=Instructor('juma', 'juma', 21, 'kenya', 4)
# # print(type(instructor_1))
# print(instructor_1.display())


# class Student:
#     def __init__(self, name,age,county):
#         self.name=name
#         self.age=age
#         self.county=county
#         self.grade=[]
#     def __str__(self):
#         return f'Name: {self.name}, Age: {self.age}, County: {self.county}, Grade: {self.grade} '
#     def add_grades(self,grades):
#         self.grade.append(grades)
#         return self.grade
#     def average_grade(self):
#         if not self.grade:
#             return 0
#         else:
#             return sum(self.grade)/len(self.grade)
        
#     def display(self):
#         average=self.average_grade()
#         return (f'Name: {self.name}, Age: {self.age}, County: {self.county}, Grade: {self.grade}, Average: {average}')
    
# studentX=Student('Jude',20,'Kitui')
# studentX.add_grades(90)
# studentX.add_grades(71)
# studentX.add_grades(68)
# studentX.add_grades(84)
    
# print(studentX.average_grade())
# print(studentX.display())

import random as r
from random import choice
for y in range(4):
    x=r.random()
    print(x)   
    
numbers=[2,45,67,88,43,'Bus', 'Bible', 'money', 'School','Wifi','Prayers']
print(choice(numbers))       
