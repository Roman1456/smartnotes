from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.resize(700,500)

qest_lbl = QLabel("Список заміток")
qest_lbl1 = QLabel("Список тегів")

answer_list = QListWidget()
answer_list1 = QListWidget

answer_text = QTextEdit()

answer_edit = QLineEdit()

qest_btn = QPushButton("Створити замітку")
qest_btn1 = QPushButton("Видалити зімітку")
qest_btn2 = QPushButton("Зберегти замітку")
qest_btn3 = QPushButton("Додати до замітки")
qest_btn4 = QPushButton("Відкріпити від замітки")
qest_btn5 =QPushButton("Шукати замітки потегу")



h1 = QVBoxLayout()


h2 = QVBoxLayout()
h2.addWidget(qest_lbl)

main_line = QHBoxLayout()






















window.show()
app.exec()
