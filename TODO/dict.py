#working with dictionary
fame=dict(name='Mainoo',age= 19 ,gender= 'male')
print(fame.values())
print(fame.keys())
#use for loop
for w in fame.values():
    print(w)
#add items


fame.update(dict(height= 180))
#or fame.update({'height': 180})
print(fame.values())

#getting items as in tuple 
print(fame.items())

#changing items
fame['age']=20
print(fame.items())

#remove items
fame.pop('height')
print(fame.items())
#popitem() removes the last item
print(fame.popitem())

#nesting dictionaries
student1={
    'name': 'lion',
    'age': 19,
    'gender':'male',
    'height': 180
}
student2={
    'name': 'Fay',
    'age': 20,
    'gender':'female',
    'height': 170
}
student3={
    'name': 'Joseph',
    'age': 21,
    'gender':'male',
    'height': 175
}
student4={
    'name': 'Mary',
    'age': 22,
    'gender':'female',
    'height': 165
}
Nested_dict={
    'Student1':student1,
    'Student2':student2,
    'Student3':student3,
    'Student4':student4
}
print(Nested_dict)


#loops
p=0
while p<5:
    p=p+1
    if p==3:
        continue
    print(p, end='')