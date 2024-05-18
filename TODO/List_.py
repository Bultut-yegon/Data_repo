this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:5])#This will return the items from position 2 to 5.
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included
print(this_list[:4])#item in index 4 is not included
print(this_list[3:])#includes the item in index 3 to the end
if 'mango' in this_list:
    print('yes')
if 'fruit' not in this_list:
    print('Actually not there')
    
    #replacing elements in a list    
this_list[2:3]=list(('guavas','lemons'))
print(this_list)
#inserting elemets without removing any element in the list, specified index is needed
this_list.insert(3,'berry')

#adding items to the end of a list, the rear part
this_list.append('juice')
print(this_list)

#extending a list using extend() function. Joining two lists
todo=list(('book','pen','pencil','board'))
this_list.extend(todo)
print(this_list)#prints the contents in thislist and todo list.
#extend() function can also add any iterable, including sets,dict and tuples
tup=('chem','math','Eng','Kis')
this_list.extend(tup)
print(this_list)
#remove() keyword removes a specified item.
this_list.remove('Eng')
print(this_list)
#To remove a specified index, we use pop() keyword.
this_list.pop(3)
print(this_list)
#if you do not specify the index, pop() removes the last element
#pop() used in stacks, removes the last element that was inserted, from the top
this_list.pop()
print(this_list)
#del() keyword also removes item at a specified index
del this_list[6]
print(this_list)
#clear() method empties the list.
bave=list(('was','were','is','are','they'))
print(bave)
bave.clear()
print(bave)
#looping in a list using for loop
for element in this_list:
    print(element)
for i in range(len(this_list)):
    print(i,this_list[i])

#using while loop
x=0
while x< len(this_list):
    print(x,this_list[x])
    x=x+1
    
#creating a new list with thislist elements containing a certain letter. List comprehension using for loop.
new=[]
for j in this_list:
    if 'n' in j:
        new.append(j)       
print(new) #prints every element in thislist having letter 'n'
#this can be done using one line of code.
xamp=[v for v in this_list if 'a' in v]#appends every element with letter 'a' in xamp
print(xamp)
#newlist = [expression for item in iterable if condition == True](syntax)
same=[s for s in range(10) if s%2==0]
print(same)
#setting values in a list to upper case or capitalize the first letter in each element( .upper() and .capitalize() methods respectively
form=[d.capitalize() for d in this_list if 'b' in d]
print(form)
#returning a certain element instead of another one

dizz=[c if c!='book' else 'book_materials' for c in this_list]
print(dizz)
#Sorting of lists.
#sorting them alphanumerically using sort() keyword
this_list.sort()#sorts the list in ascending order by default
print(this_list)
#sorting the list in ascending order, you place the parameter reverse=true
this_list.sort(reverse=True)
print(this_list)

#customizing sort function

def rerun(w):
    return abs(w-50)
numbers=list((12,23,45,67,89,100,77,50)    
numbers.sort(key=rerun)
print(numbers)
#By default sort() function is case sensitive. It sorts out words that have capital letters before the words with small letters.
#so we use key=str.lower to solve this issue
names=list(('James','john','Paulina','henry','Meshack','risper'))
names.sort(key=str.lower)
print(names)

#The order of the list can also be reversed using reverse() keyword
names.reverse()
print(names)
#copying of lists.
#method:copy() and list()
My_list=this_list.copy()
print(My_list)
My_word=list(My_list)
print(My_word)

#Joining lists.
#Either use for loop or extend()
me=list((22,34,56,78,90,100))
her=list((12,23,34,45,56,67))
#for loop
for x in her:
    me.append(x)
print(me) 
#extend keyword
me.extend(her)
print(me)