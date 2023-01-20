from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox

app = QApplication([])
main_win = QWidget()
main_win.resize(400, 150)
main_win.setWindowTitle('Викторина!')
text = QLabel('В каком году была основана Алгортимика?')
#message boxы
victory_win = QMessageBox()
lose_win = QMessageBox()
victory_win.setWindowTitle('ПОБЕДА АРГЕНТИНЫ!')
victory_win.setText('А ты неплох')
lose_win.setWindowTitle('франция проиграла(')
lose_win.setText('Иди читай википедию')

button1 = QRadioButton('2015')
button2 = QRadioButton('2016')
button3 = QRadioButton('2014')
button4 = QRadioButton('2017')

h1_line = QHBoxLayout()
h2_line = QHBoxLayout()
h3_line = QHBoxLayout()
v_line = QVBoxLayout()

h1_line.addWidget(text, alignment = Qt.AlignCenter)
h2_line.addWidget(button1, alignment = Qt.AlignCenter)
h2_line.addWidget(button2, alignment = Qt.AlignCenter)
h3_line.addWidget(button3, alignment = Qt.AlignCenter)
h3_line.addWidget(button4, alignment = Qt.AlignCenter)

v_line.addLayout(h1_line)
v_line.addLayout(h2_line)
v_line.addLayout(h3_line)

def show_win():
    if button2.isChecked():
        victory_win.show()
        
    else:
        lose_win.show()   


button1.clicked.connect(show_win)
button2.clicked.connect(show_win)
button3.clicked.connect(show_win)
button4.clicked.connect(show_win)

main_win.setLayout(v_line)
main_win.show()
app.exec()