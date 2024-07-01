thisset = {"apple", "banana", "cherry"}  # find whether an element is in a set

print("banana" in thisset)


# In[7]:


thisset = {"apple", "banana", "cherry"} # printing elements one by one in a set

for x in thisset:
  print(x) 


# In[8]:


thisset = {"apple", "banana", "cherry"} # adding single element in a set

thisset.add("orange")

for y in thisset:
    print(y)

print(thisset) 


# In[9]:


thisset = {"apple", "banana", "cherry"}  # adding element or merging sets
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset) 


# In[12]:


thisset = {"apple", "banana", "cherry"} # removing elements from sets

thisset.remove("banana")

print(thisset) 


# In[13]:


# union in sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) 
set4=set1.intersection(set2)
print(set4)


# In[14]:


intersection of unions
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x) 


# In[15]:


# symmetric in set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x) 


# In[16]:


thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets to make a tuple
print(thistuple)


# In[17]:


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:3])


# In[18]:


thistuple = ("apple", "banana", "cherry") # adding elements into a tuple
y = ("orange",)
thistuple += y

print(thistuple)


# In[19]:


tuple1 = ("a", "b" , "c") # joining two tuples
tuple2 = (1, 2, 3)

tuple3 = tuple2 + tuple1
print(tuple3) 


# In[20]:


Python3 code to demonstrate working of
Construct Cartesian Product Tuple list
using list comprehension
 
initialize list and tuple
test_list = [1, 4, 6, 7]
test_tup = (1, 3)
 
# printing original list and tuple
print("The original list : " + str(test_list))
print("The original tuple : " + str(test_tup))
 
# Construct Cartesian Product Tuple list
# using list comprehension
res = [(a, b) for a in test_tup for b in test_list]
 
# printing result
print("The Cartesian Product is : " + str(res))


# In[21]:


import itertools # permutation
 
s = "ABC"

perm_set = itertools.permutations(s)
for val in perm_set:
    print(val)


# In[22]:


x = {"apple", "banana", "cherry"}  # demostraing disjoint
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z) 


# In[24]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook", "apple"}

z = x.isdisjoint(y)

print(z) 


# In[25]:


a = "Hello" # concatenate
b = "World"
c = a + b
print(c)


# In[26]:


a = "Hello"
b = "World"
c = a + " " + b
print(c)


# In[27]:


txt = "I could eat bananas all day" # partition

x = txt.partition("bananas")

print(x) 


# In[28]:


# Python code
# To reverse words in a given string
 
# input string
string = "geeks quiz practice code"
# reversing words in a given string
s = string.split()[::-1]
# l = []
for i in s:
    # appending reversed words to l
    l.append(i)
# printing reverse words
print(' '.join(l))

supermarket='My best supermarket in Nairobi is Randa'
Reversed_words = []

word=supermarket.split()[::-1]
for element in word:
    Reversed_words.append(element)
print(' '.join(Reversed_words))


# In[31]:


def isPalindrome(s):
    return s == s[::-1]
 
s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")


# In[33]:


def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(myfunc)


# In[ ]:





# In[ ]:



