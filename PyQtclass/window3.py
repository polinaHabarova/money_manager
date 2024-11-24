from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QDateEdit, QLineEdit, QPushButton, QComboBox, QMessageBox
from DataBase.utils_db import add_cost
from PyQtclass.image_label import ImageTextLabel, Line_widget

class Window3(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = ImageTextLabel('Вывод денег', 'image/title/forest.jpeg')
        layout.addWidget(label)

        line = Line_widget()
        layout.addWidget(line)
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

        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setText("Информация загружена")
        msg_box.setWindowTitle("ИНФОРМАЦИОННОЕ СООБЩЕНИЕ")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)

        msg_box.exec()