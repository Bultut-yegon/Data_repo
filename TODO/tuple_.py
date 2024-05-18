#immutable Python data structure
#tuples are created by using brackets or tuple() keyword
#Example
this_tuple=tuple(('shoe','bag','book','shelf',22,'desk',True))#or this_tuple=('shoe','bag','book','shelf',22,'desk',True)
print(this_tuple)
#Tuples are accessed by specifying their elements
print(this_tuple[2])
#indexing in tuples is same as that of list
'''tuple is unchangable.The only way it can be changed is by converting the tuple into a list and then change the elements then convert the list back to tuple that is after changing it.'''
#Example
book=tuple(('horizon','Egocen','Look warm','Justice','yowning'))
slide=list(book)
print(slide)
print(type(slide))
slide[2]='Bellow'
changed=tuple(slide)
print(changed)
print(type(changed))
#tuple length
print(len(changed))
#to remove an element in a tuple, convert it to list, remove the element and convert back to tuple
#del my_tuple #to delete the whole tuple
#unpacking a tuple
fruits=tuple(('mangoes','lemons','grapes','bananas'))
(w,x,y,z)=fruits
print(w)
print(x)
print(y)
print(z) #The number of variables must match the number of values in the tuple.

#if the number of variables is less than the number of values,use * to accommodate for the remaining values
fruit=tuple(('mangoes','lemons','grapes','bananas'))
(a,b,*c)=fruit
print(a)
print(b)
print(c)
#looping through a tuple
#using for loop
for j in fruit:
    print(j)
#using range() and len()
for k in range(len(fruit)):
    print(k,fruit[k])
#using while loop
w=0
while w < len(fruit):
    print(fruit[w],w)
    w=w+1