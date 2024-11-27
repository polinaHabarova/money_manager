from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QDateEdit, QLineEdit, QPushButton, QMessageBox
from DataBase.utils_db import add_refill
from PyQtclass.image_label import ImageTextLabel, Line_widget

class Window2(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = ImageTextLabel('Пополнения', 'image/title/forest.jpeg')
        layout.addWidget(label)

        line = Line_widget()
        layout.addWidget(line)

        data = QLabel('Введите дату пополнения счёта')
        data.setStyleSheet("""
                            QLabel {
                                font-size: 24px;
                                font-family: 'Arial';
                                color: black;
                                padding: 20px;  
                                border-radius: 10px;
                                text-align: center;
                            }
                        """)

        self.data_input = QDateEdit()
        self.data_input.setDisplayFormat('dd.MM.yyyy')

        money = QLabel('Введите количество полученных денег')
        money.setStyleSheet("""
                            QLabel {
                                font-size: 24px;
                                font-family: 'Arial';
                                color: black;
                                padding: 20px;  
                                border-radius: 10px;
                                text-align: center;
                            }
                        """)

        self.money_input = QLineEdit()

        button = QPushButton('Отправить')
        button.setStyleSheet(
            f"""
                                    QPushButton {{
                                        background-color: #004953;
                                        color: #fcfcee;
                                        font-size: 16px;
                                        font-weight: bold;
                                        border-radius: 10px;
                                        padding: 10px;
                                    }}
                                    QPushButton:hover {{
                                        background-color: #2a6478;
                                    }}
                                    """)
        button.clicked.connect(self.get_money)


        layout.addWidget(data)
        layout.addWidget(self.data_input)
        layout.addWidget(money)
        layout.addWidget(self.money_input)
        layout.addWidget(button)

        self.setLayout(layout)

    def get_money(self):
        add_refill(self.money_input.text(), self.data_input.date().toString('dd.MM.yyyy'))

        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setText("Информация загружена")
        msg_box.setWindowTitle("ИНФОРМАЦИОННОЕ СООБЩЕНИЕ")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)

        msg_box.exec()

