# #working with dictionary
# fame=dict(name='Mainoo',age= 19 ,gender= 'male')
# print(fame.values())
# print(fame.keys())
# #use for loop
# for w in fame.values():
#     print(w)
# #add items


# fame.update(dict(height= 180))
# #or fame.update({'height': 180})
# print(fame.values())

# #getting items as in tuple 
# print(fame.items())

# #changing items
# fame['age']=20
# print(fame.items())

# #remove items
# fame.pop('height')
# print(fame.items())
# #popitem() removes the last item
# print(fame.popitem())

# #nesting dictionaries
# student1={
#     'name': 'lion',
#     'age': 19,
#     'gender':'male',
#     'height': 180
# }
# student2={
#     'name': 'Fay',
#     'age': 20,
#     'gender':'female',
#     'height': 170
# }
# student3={
#     'name': 'Joseph',
#     'age': 21,
#     'gender':'male',
#     'height': 175
# }
# student4={
#     'name': 'Mary',
#     'age': 22,
#     'gender':'female',
#     'height': 165
# }
# Nested_dict={
#     'Student1':student1,
#     'Student2':student2,
#     'Student3':student3,
#     'Student4':student4
# }
# print(Nested_dict)


# #loops
# p=0
# while p<5:
#     p=p+1
#     if p==3:
#         continue
#     print(p)
    
# num1=[1,2,3]
# num2=[10,11,12]
# for f in num1:
#     for g in num2:
#         print(f,g)   
# #functions
# #POA(positional only arguments)=> (,/)
# def place(a,/):
#     print(a)
# place(7)
# #KW(keyword only arguments)=> (*,)
# def place(a,*,b):
#     print(a)
#     print(b)
# place(7,b=8)
# #(*args) and (**kwargs)
# def num(*numbers):
#     print(numbers)
# num(1,2,3,4,5,6,7,8,9,10)

# def num_1(**nums):
#     print(nums)
# num_1(a=1,b=2,c=3,d=4)

config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "user": "myapp",
        "password": "s3cr3t"
    },
    "email": {
        "smtp_server": "smtp.gmail.com",
        "smtp_port": 587,
        "from_address": "noreply@myapp.com"
    },
    "logging": {
        "level": "INFO",
        "file_path": "/var/log/myapp.log"
    }
}

print(config['database']['port'])