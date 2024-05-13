def person(name,age,country):
    print('Welcome ',name)
    print('Your age is ',age)
    print('Your country is ',country)
    
number=int(input('Enter a number '))
for x in range(number):
    name=input("Enter your name: ").lower()
    age=int(input("Enter your age"))
    country=input("Enter your country: ").lower()
    person(name,age,country)