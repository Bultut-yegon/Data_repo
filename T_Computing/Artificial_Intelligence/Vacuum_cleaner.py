import random
'''Importing the random module:
The random module is imported to generate random values, which will 
be used to simulate the distribution of dirt in the room.'''
def display(room):
    print(room)
''' Defining the display() function
   The display() function is defined to print the 
   current state of the room, represented by a 2D list room.'''
room=[
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]
]
print("All rooms are dirty")
'''(Printing the initial state of the room:
The initial state of the room is printed, indicating that "All rooms are dirty.")'''
display(room)
x=0
y=0
while x<4:
    while y<4:
        room[x][y]=random.choice([0,1])
        '''Simulating the random distribution of dirt:
Two nested loops are used to iterate through the room, and for each cell, a random choice of 0 (clean) or 
1 (dirty) is assigned using the random.choice() function.'''
        y+=1
    x+=1
    y=0
print("Before cleaning, detect random dirt in this room")
display(room)

x=0
y=0
z=0
while x<4:
    while y<4:
        if room[x][y]==1:
            print("Vacuum is now in location ",x,y)
            
            room[x][y]=0
            print('Cleaned ',x,y)
            z+=1
        y+=1
    x+=1
    y=0
    
pro=(100-((z/16)*100))
print('Room is now clean.  ')
display(room)
print('Performance is: ',pro, '%')

print(display.__doc__)
    