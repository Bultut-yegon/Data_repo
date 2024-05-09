#print(Initialized_list)
# This is a List: use square brackets
sure_list=[23,19,25,27,39,30,41,29]
print(sure_list)
user=sure_list[1:5:3]
print(user)

sure_list.append(59)
print(sure_list)

del sure_list[2]

print(sure_list)

#This is a tuple: Cannot modify their values, use parentheses
months=("Jan", "March" , "April", "May", "June", "July", "August", "September", "Oct", "Nov", "December")
print(months[-1])

#Dictionary: use curly braces
people={"John":20,"Nora":33,"Janitor":21,"Swahili":"Not recognized"}
print(people)

#dict() method can be used
people1=dict(Peter=23,Mary=19,Packer=10,Cookie=36)
print(people1)

#modifying dictionary values
people1["Packer"]=90
print(people1)

del people1["Cookie"]
print(people1)

#input()-> method
#school=input("Name of the school: ")
#course=input("Course please: ")
#print("The school is ",school," doing ",course)

enter=input("Please enter 1 or 4: ")
if enter=="1":
    print("You have one relationship issue")
elif enter=="4":
    print("You have four relationships issue")
else:
    print("You entered incorrect input")
    
#inline if
#print("This is the first relationship" if user=="1" else "I had many relationships")
 
#for loop
fruits=["apple", "orange", "banana", "strawberry", "lemons","guava","green"]
for index, fruit in enumerate(fruits):
    print(index,fruit)

#looping in a dictionary
guys={"Alexander": 22, "Kart": 23, "Flex": 18, "Mainoo":18, "Garnacho":19} 
for i,j in guys.items():
    print("Name=%s, age= %d" %(i,j ) )  
    
#loop through a string
must=("Can you come over tonight?")
for i in must:
    print(i)      

#range of numbers
#use range() method.
#range(start,end,step) 

for k in range(6): # end is 6. start is 0 by default
    print(k)
    
for g in range(2,6):# start is 2 and end is 6(6-1). step is 1 by default
    print(g)
    
for h in range(4,12,2):# start is 4 and end is 12(12-2). step is 2
    print(h)
    
#while loop
count=6
while count>0:
    print("count  :",count)
    count=count-1 
    
#break 
f=0
for m in range(4):
    f=f+3
    print("m :",m,"f :",f)
    if f==9:
        break
    
#continue
b=2
for u in range(4):
    b=b+2
    print("u :",u,"b :",b)
    if b==6:
        continue
    print("Wow")    
          
# try, except
try:
    userinput1=int(input("Enter first number:"))
    userinput2=int(input("Enter second number:"))
    answer=userinput1/userinput2
    print(answer)
    file=open("missing.txt", "r")
except ValueError:
    print("Please enter a number.You did not entered a number")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print("Unknown error:", e)
    
print(answer)    
    
#functions and modules

#function with several arguments

def add(*num):
    sum=0
    for r in num:
        sum=sum+r
    #sum=sum+r
    return sum

print(add(23,33,44,55,66,77,88))

#function with keyworded arguments
def keyword(**age):
    for i,j in age.items():
        print("Name = ",i," , age = ",j)
        
print(keyword(Jones=20,Bult=20))
#formal arguments
#def user(farg,*args,**kwargs):
 #   for e in range(0,len(args)):
  #      print(e)

#import mod
#prime=mod.PrimeNumber(23)
#print(prime)   

#File handling
     
file=open ('test.txt', 'r')
firstline=file.readline()
secondline=file.readline()
print(firstline)
print(secondline)
file.close()

#using for loop to read files
f=open('test.txt','r')
for line in f:
    print(line,end='')
f.close()    
    
#writing to txt files 
write=open('test.txt','a')
write.write('\n Python is fun')
write.write('\n Writing to txt files in Python is easy!')
write.close()


   
    