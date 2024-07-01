# print("Hello user",'Welcome ','to our system' , sep='-',end='*''\n')
# print('Hello')#sep and end keywords in print() function
#end prints what is at the end after print function is executed
#sep keyword specifies the separator used after each word
# print(0o234)
# print(0o22)#octal number, its prefix is 0o(zero-o)

#hexadecimal number, its prefix is 0x(zero-x)
# print(0x23)
# print(0x22)
#binary number, its prefix is 0b(zero-b)
# print(0b101)
# print(0b10)

# skipping characters in strings
# use / 
# print('My friend /" is Zakayo')

# i=0
# while i<10:
#     name=input('Enter your username: ')
#     print('Hey ',name, ' you have secured your flight ticket ')
#     i=i+1
# else:
#     print('There is no space available. Try next time')
    
# number=int(input('Number: '))
# number_1=map(lambda x: x**2,number)
# print(number_1)

#filter
# boats=[1,2,3,4,5,6,7,8,9]
#even_number=filter(lambda x: x%2==0,boats)

# num=int(input('Enter the number of people: '))
# for j in range(num):
#     name=input('Enter your name: ')
#     print('You are ', name)
# k=0
# while k<num:
#     print('Welcome')
# else:
#     print('There is no space available. Try next time')
# import timeit as t
# new_list=[m**2 for m in boats if m%2==0]
# print(t.timeit( '[m**2 for m in range(10) if m%2==0]', number=100000))
# print(new_list) #list comprehension
# import math

# print(math.factorial(5))
# import random
# for f in range(10):
#     c=random.random()
#     print(c)
#print(random.randint(3,6))
# value=[2,3,4,5,6,7,8,9]
# print(random.choice(value))

# num=[22,33,44,55,66,77,88,99]
# max=num[0]
# for i in num:
#     if i>max:
#         max=i
# print(max)

# n
# def safe_list_access(lst, index):
#     try:
#         return lst[index]
#     except IndexError:
#         print("Index out of range!")
#         return None

# # Example usage
# my_list = [1, 2, 3, 4, 5]
# index = 10

# result = safe_list_access(my_list, index)
# if result is not None:
#     print(f"Element at index {index}: {result}")
# else:
#     print("Failed to access element.")

# def Put_dict(text):
#     reading=open(text.rstrip)
#     diction={}
#     for word in reading:
#         word=word.strip()
#         if word in diction:
#             continue
#         else:
#             diction.append()
            
# take=Put_dict('./Tasks.txt')
# print(take)

# #counting thenumber of letters
# words=input('enter a string : ')
# doso=dict()
# for letter in words:
#     doso[letter]=doso.get(letter,0)+1
# print(doso)


# file=input('Enter the text file: ')

# try:
#     filename=open(file)
# except:
#     print('No such existing file', file)
#     exit()
    
# conut={}

# for line in filename:
#     wordings=line.split()
#     for each in wordings:
#         if each in conut:
#             conut[each]+=1
#         else:
#             conut[each]=1
# print(conut)

# docs={'a':89,'b':25,'c':194,'d':90,'e':39}
# # lists=[]

# for key, val in docs.items():
#     lists=list(docs)
#     # print(val,key)  
#     lists=lists.append((val,key))
    
#     lists=lists.sort(reverse=True) 
#     print(lists)

# import random
# for j in range(10):
#     x=random.random()
#     print(x)

def change(deg):
          