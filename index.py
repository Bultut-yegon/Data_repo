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
people={"John":20,"Kamau":33,"Janto":21,"Swaleh":"Not recognised"}
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
          
               