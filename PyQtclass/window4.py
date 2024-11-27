from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QMessageBox
from PyQtclass.image_label import ImageTextLabel, Line_widget
from DataBase.utils_db import get_allData, delete_data


class Window4(QWidget):
    def __init__(self):
        super().__init__()
        self.index = 0

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.create_button(self.index)

    def create_button(self, index):
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
        self.clear_layout(self.main_layout)

        label_text = ImageTextLabel('Изменения в БД', 'image/title/forest.jpeg')
        self.main_layout.addWidget(label_text)

        line = Line_widget()
        self.main_layout.addWidget(line)

        button_layout = QHBoxLayout()
        for button_data in self.button_list[index]:
            button = QPushButton(f"id{button_data['id']}")
            if button_data["color"] == "red":
                button.setStyleSheet(
                    """
                    QPushButton {
                        background-color: #cc0605;
                        color: #fcfcee;
                        font-size: 16px;
                        font-weight: bold;
                        border-radius: 10px;
                        padding: 10px;
                    }
                    QPushButton:hover {
                        background-color: #ce2029;
                    }
                    """
                )
            else:
                button.setStyleSheet(
                    """
                    QPushButton {
                        background-color: #71bc78;
                        color: #fcfcee;
                        font-size: 16px;
                        font-weight: bold;
                        border-radius: 10px;
                        padding: 10px;
                    }
                    QPushButton:hover {
                        background-color: #aaf0d1;
                    }
                    """
                )
            button.clicked.connect(self.create_change_data_handler(button_data["id"], button_data["color"]))
            button_layout.addWidget(button)
        self.main_layout.addLayout(button_layout)

        nav_layout = QHBoxLayout()
        button_back = QPushButton('<-')
        button_next = QPushButton('->')

        for btn in [button_back, button_next]:
            btn.setStyleSheet(
                """
                QPushButton {
                    background-color: #004953;
                    color: #fcfcee;
                    font-size: 16px;
                    font-weight: bold;
                    border-radius: 10px;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: #2a6478;
                }
                """
            )

        button_back.clicked.connect(self.back)
        button_next.clicked.connect(self.next)
        nav_layout.addWidget(button_back)
        nav_layout.addWidget(button_next)

        self.main_layout.addLayout(nav_layout)

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            else:
                sub_layout = item.layout()
                if sub_layout:
                    self.clear_layout(sub_layout)

    def create_change_data_handler(self, id, color):
        return lambda: self.change_data(id, color)

    def back(self):
        if self.index > 0:
            self.index -= 1
            self.create_button(self.index)

    def next(self):
        if self.index < len(self.button_list) - 1:
            self.index += 1
            self.create_button(self.index)

    def change_data(self, id, color):
        delete_data(id, color)
        self.create_button(self.index)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setText("Данные удалены")
        msg_box.setWindowTitle("ИНФОРМАЦИОННОЕ СООБЩЕНИЕ")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)

        msg_box.exec()
