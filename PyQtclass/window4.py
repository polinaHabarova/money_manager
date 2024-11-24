from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QMessageBox
from PyQtclass.image_label import ImageTextLabel, Line_widget

from DataBase.utils_db import get_allData, delete_data
class Window4(QWidget):
    def __init__(self):
        super().__init__()
        self.index = 0
        result1, result2 = get_allData()
        self.button_list = []
        button4 = []
        for i in result1:
            if len(button4) == 4:
                self.button_list.append(button4)
                button4 = []
            button4.append({
                "id": i[0],
                "color": 'green'
            })
        for i in result2:
            if len(button4) == 4:
                self.button_list.append(button4)
                button4 = []
            button4.append({
                "id": i[0],
                "color": 'red'
            })
        if len(button4) != 0:
            self.button_list.append(button4)
        self.create_button(self.index)

    def create_button(self, index):
        layout = QVBoxLayout()

        label_text = ImageTextLabel('Изменение данных', 'image/title/forest.jpeg')
        layout.addWidget(label_text)

        self.buttons = []

        line = Line_widget()
        layout.addWidget(line)

        button_layout = QHBoxLayout()
        for i in self.button_list[index]:
            button = QPushButton(f"id{i['id']}")

            button.setStyleSheet(
                f"""
                QPushButton {{
                    background-color: #ffa474;
                    color: #fcfcee;
                    font-size: 16px;
                    font-weight: bold;
                    border-radius: 10px;
                    padding: 10px;
                }}
                QPushButton:hover {{
                    background-color: #fdd9b5;
                }}
                """)

            button.clicked.connect(lambda checked, index=f"{i['id']}-{i['color']}": self.change_data(index))
            self.buttons.append(button)
            button_layout.addWidget(button)

        layout.addLayout(button_layout)
        horisontal_box = QHBoxLayout()
        button1 = QPushButton('<-')
        button1.setStyleSheet(
            f"""
                                   QPushButton {{
                                       background-color: #ffa474;
                                       color: #fcfcee;
                                       font-size: 16px;
                                       font-weight: bold;
                                       border-radius: 10px;
                                       padding: 10px;
                                   }}
                                   QPushButton:hover {{
                                       background-color: #fdd9b5;
                                   }}
                                   """)

        button2 = QPushButton('->')
        button2.setStyleSheet(
            f"""
                                   QPushButton {{
                                       background-color: #ffa474;
                                       color: #fcfcee;
                                       font-size: 16px;
                                       font-weight: bold;
                                       border-radius: 10px;
                                       padding: 10px;
                                   }}
                                   QPushButton:hover {{
                                       background-color: #fdd9b5;
                                   }}
                                   """)

        button1.clicked.connect(self.back)
        button2.clicked.connect(self.next)
        horisontal_box.addWidget(button1)
        horisontal_box.addWidget(button2)
        layout.addLayout(horisontal_box)

        if self.layout() is not None:
            for i in reversed(range(self.layout().count())):
                widget = self.layout().itemAt(i).widget()
                if widget is not None:
                    widget.deleteLater()
        self.setLayout(layout)

    def back(self):
        if self.index != 0:
            self.index -= 1
            self.create_button(self.index)

    def next(self):
        if len(self.button_list) - 1 != self.index:
            self.index += 1
            self.create_button(self.index)

    def change_data(self, index):
        id, color = index.split('-')
        delete_data(id, color)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setText("Данные удалены")
        msg_box.setWindowTitle("ИНФОРМАЦИОННОЕ СООБЩЕНИЕ")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)

        msg_box.exec()



