import json

from PyQt5.QtWidgets import *

app = QApplication([])

notes={}
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


h1 = QVBoxLayout()

h1.addWidget(qest_lbl)
h1.addWidget(answer_list)
h1.addWidget(qest_btn)
h1.addWidget(qest_btn1)
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

def read_data():
    global notes
    with open("database.json","r", encoding="utf-8") as file:
        notes = json.load(file)

def write_data():
    global notes
    with open("database.json","w", encoding="utf-8") as file:
        json.dump(notes,file, ensure_ascii=False,indent=4)
read_data()
answer_list.addItems(notes)

def vmist_note():
    name = answer_list.selectedItems()[0].text()
    answer_text.setText(notes[name]["Вміст"])

answer_list.itemClicked.connect(vmist_note)

def change_note():
    name = answer_list.selectedItems()[0].text()
    notes[name]["Вміст"]=answer_text.toPlainText()
    write_data()

qest_btn2.clicked.connect(change_note)




def add_note():
    res, ok =QInputDialog.getText(window, "Ведення" , "Ведіть назву замітку")
    if ok:
        notes[res] = {
            "Вміст": "",
            "Теги": []
        }
        write_data()

qest_btn.clicked.connect(add_note)
window.show()
app.exec()
