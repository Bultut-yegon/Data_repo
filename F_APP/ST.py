#imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QVBoxLayout,QHBoxLayout

#settings
app=QApplication([])
main_window=QWidget()
main_window.setWindowTitle("First Project")
main_window.resize(350, 250)

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

main_window.setLayout(master)



main_window.setLayout(master)

main_window.show()
app.exec_()
                                                                                                                                                                                                                                                                                                            

