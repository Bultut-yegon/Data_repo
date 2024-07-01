# def person(name,age,country):
#     print('Welcome ',name)
#     print('Your age is ',age)
#     print('Your country is ',country)
    
# number=int(input('Enter a number '))
# for x in range(number):
#     name=input("Enter your name: ").lower()
#     age=int(input("Enter your age"))
#     country=input("Enter your country: ").lower()
# #     person(name,age,country)
# n = int(input("Enter a positive integer: "))
# a, b = 0, 1
# while a <= n:
#     print(a, end=" ")
#     a, b = b, a+b
# print()
# from sympy import factorial


# num=int(input('Number'))
# j=1
# if num<=0:
#     print('Must be greater than zero')
# else:
#     k=1
#     while k<=num:
#         j=j*k
#         k=k+1
#         print(j) 

# output=1
    
# for b in range(1, num+1):
#     output*=b
#     print(output)

#     print(num)
# h=3
# while h <10:
#     h=h+1
#     if h==6:
#         continue
#     print(h)
    
# x=4
# while x<=8:
#     print(x)
#     if x==6:
#         break
#     x+=1

def update(d):
    print(id(d))
    d=8
    print(id(d))
    print(d)
a=90
print(id(a))
use=update(a)
print(use)
