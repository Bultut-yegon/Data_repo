from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QVBoxLayout,QHBoxLayout
from random import choice

#settings
app=QApplication([])
main_window=QWidget()
main_window.setWindowTitle("First Project")
main_window.resize(350, 350)

title=QLabel("Starting position")

text=QLabel('start')
text_1=QLabel('Start')
text_2=QLabel('Start')

button1=QPushButton('Click')
button2=QPushButton('Click')
button3=QPushButton('Click')

master=QVBoxLayout()
row1=QHBoxLayout() # type: ignore

row2=QHBoxLayout() # type: ignore
row3=QHBoxLayout() # type: ignore

row1.addWidget(title,alignment=Qt.AlignCenter)

row2.addWidget(text,alignment=Qt.AlignCenter)
row2.addWidget(text_1,alignment=Qt.AlignCenter)
row2.addWidget(text_2,alignment=Qt.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

master.addLayout(row1)
master.addLayout(row2)
master.addLayout(row3)
#My random words
words=['apple','orange','Python developer','banana','Computer Science',
       'Data Science','mango','career','pineapple','grapes','watermelon'
       ,'strawberry','Machine Learning','Artificial Intelligence','cherry'
       ,'peach','Bible','BMW','Audi','App','Developer','Game','Manchester United']
def random_words():
    return choice(words)

def change_text():
    select=choice(words)
    text.setText(select)
    
    
def change_text1():
    select=choice(words)
    text_1.setText(select)
    

def change_text2():
    select=choice(words)
    text_2.setText(select)
        
    
    

main_window.setLayout(master)


#events
button1.clicked.connect(change_text)
button2.clicked.connect(change_text1)
button3.clicked.connect(change_text2)



# main_window.setLayout(master)

main_window.show()
app.exec_()
                                                                                                                                                                                                                                                                                               

