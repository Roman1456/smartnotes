from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.resize(700,500)

qest_lbl = QLabel("Список заміток")
qest_lbl1 = QLabel("Список тегів")

answer_list = QListWidget()
answer_list1 = QListWidget()

answer_text = QTextEdit()

answer_edit = QLineEdit()

qest_btn = QPushButton("Створити замітку")
qest_btn1 = QPushButton("Видалити зімітку")
qest_btn2 = QPushButton("Зберегти замітку")

qest_btn3 = QPushButton("Додати до замітки")
qest_btn4 = QPushButton("Відкріпити від замітки")
qest_btn5 =QPushButton("Шукати замітки потегу")

mine_line = QHBoxLayout()

mine_line.addWidget(answer_text)

h2 = QHBoxLayout
h1 = QVBoxLayout()
h1.addWidget(qest_lbl)
h1.addWidget(answer_list)
h1.addWidget(qest_btn)

h2.addWidget(qest_btn1)

h1.addWidget(qest_btn2)


h1.addWidget(qest_lbl1)
h1.addWidget(answer_list1)
h1.addWidget(answer_edit)
h1.addWidget(qest_btn3)
h1.addWidget(qest_btn4)
h1.addWidget(qest_btn5)

h1.addStretch(1)
mine_line.addLayout(h1)





window.setLayout(mine_line)
window.show()
app.exec()
