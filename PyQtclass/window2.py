from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QDateEdit, QLineEdit, QPushButton
from DataBase.utils_db import add_refill

class Window2(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel('Поступление средств')
        layout.addWidget(label)

        data = QLabel('Введите дату поступления средств')
        self.data_input = QDateEdit()
        self.data_input.setDisplayFormat('dd.MM.yyyy')

        money = QLabel('Введите количество полученных денег')
        self.money_input = QLineEdit()

        button = QPushButton('Отправить')
        button.clicked.connect(self.get_money)


        layout.addWidget(data)
        layout.addWidget(self.data_input)
        layout.addWidget(money)
        layout.addWidget(self.money_input)
        layout.addWidget(button)

        self.setLayout(layout)

    def get_money(self):
        add_refill(self.money_input.text(), self.data_input.date().toString('dd.MM.yyyy'))

