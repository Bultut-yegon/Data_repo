num=[2,3,5,6,7,87,54,332,43]
print(num.sort(reverse=True))

#setp3s
a_sub={1,2,3,4,5,6,6}
a_sub1={5,6,7,7,8,9}
sub=a_sub.union(a_sub1)
a_sub | a_sub1
print(sub)
for value in sub:
    print(value)
    
import time as t 
print(t.time())       