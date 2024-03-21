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

school=input("Name of the school: ")
course=input("Course please: ")
print("The school is ",school," doing ",course)
