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
    answer_list1.clear()
    answer_list1.addItems(notes[name]["Теги"])


answer_list.itemClicked.connect(vmist_note)

def change_note():
    name = answer_list.selectedItems()[0].text()
    notes[name]["Вміст"]=answer_text.toPlainText()
    write_data()

qest_btn2.clicked.connect(change_note)



def delet_note():
    res, ok = QInputDialog.getText(window, "Ведення", "Ведіть назву замітку")
    if ok:
        notes.pop(res)
        answer_list.clear()
        answer_list.addItems(notes)

        write_data()

qest_btn1.clicked.connect(delet_note)

def add_note():
    res, ok =QInputDialog.getText(window, "Ведення" , "Ведіть назву замітку")
    if ok:
        notes[res] = {
            "Вміст": "",
            "Теги": []
        }
        write_data()

def add_tag():
    name = answer_list.selectedItems()[0].text()
    tag = answer_edit.text()
    notes[name]["Теги"].append(tag)
    answer_list1.clear()
    answer_list1.addItems(notes[name]["Теги"])
    write_data()

qest_btn3.clicked.connect(add_tag)

def delet_tag():
    name_note = answer_list.selectedItems()[0].text()
    name_tag = answer_list1.selectedItems()[0].text()
    notes[name_note]["Теги"].remove(name_tag)
    write_data()

qest_btn4.clicked.connect(delet_tag)

qest_btn.clicked.connect(add_note)
qest_btn1.clicked.connect(delet_note)
window.show()
app.exec()
