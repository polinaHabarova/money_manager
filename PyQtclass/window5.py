import json

from PyQtclass.image_label import ImageTextLabel, Line_widget
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox
from unicodedata import category

from DataBase.utils_db import get_allData


class Window5(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label_text = ImageTextLabel('Получить статистику', 'image/title/forest.jpeg')
        layout.addWidget(label_text)

        line = Line_widget()
        layout.addWidget(line)
        self.setLayout(layout)

        self.get_statisticButton = QPushButton('Получить статистику', self)
        self.get_statisticButton.clicked.connect(self.get_statistic)
        self.get_statisticButton.setMinimumSize(300, 300)
        layout.addWidget(self.get_statisticButton)
        self.setLayout(layout)

    def get_statistic(self):
        result1, result2 = get_allData()
        refill = []
        for i in result1:
            data = {
                "id": i[0],
                "data": i[1],
                "money": i[2]
            }
            refill.append(data)
        with open("refill_statistic.json", "w") as file_json:
            json.dump(refill, file_json, indent=4)
        cost = []
        for i in result2:
            data1 = {
                "id": i[0],
                "data": i[1],
                "money": i[2],
                "category": i[3]
            }
            cost.append(data1)
        with open("cost_statistic.json", "w") as file_json:
            json.dump(cost, file_json, indent=4)

        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setText("Данные успешно загружены в файлы")
        msg_box.setWindowTitle("ИНФОРМАЦИОННОЕ СООБЩЕНИЕ")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)

        msg_box.exec()