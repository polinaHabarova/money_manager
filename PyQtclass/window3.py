from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QDateEdit, QLineEdit, QPushButton, QComboBox
from DataBase.utils_db import add_cost

class Window3(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel('Вывод денег')
        layout.addWidget(label)
        self.setLayout(layout)

        data = QLabel('Введите дату траты средств')
        self.data_input = QDateEdit()
        self.data_input.setDisplayFormat('dd.MM.yyyy')

        money = QLabel('Введите количество потраченных денег')
        self.money_input = QLineEdit()

        category = QLabel('Выберите категорию на которую были потрачены деньги')
        self.category_input = QComboBox()
        self.category_input.addItems(['Образование', 'Развлечения', 'Еда', 'Прочее'])


        button = QPushButton('Отправить')
        button.clicked.connect(self.spend_money)

        layout.addWidget(data)
        layout.addWidget(self.data_input)
        layout.addWidget(money)
        layout.addWidget(self.money_input)
        layout.addWidget(category)
        layout.addWidget(self.category_input)
        layout.addWidget(button)


        self.setLayout(layout)

    def spend_money(self):
        add_cost(self.money_input.text(), self.data_input.date().toString('dd.MM.yyyy'), self.category_input.currentText())
