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