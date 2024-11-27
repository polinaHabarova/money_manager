from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QTextBrowser
import requests
from DataBase.utils_db import get_refill, get_cost
from PyQtclass.image_label import ImageTextLabel, Line_widget


class Window1(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label_text = ImageTextLabel('Меню', 'image/title/forest.jpeg')
        layout.addWidget(label_text)


        line = Line_widget()
        layout.addWidget(line)
        input = QLabel('Получено всего')
        input.setStyleSheet("""
                            QLabel {
                                font-size: 24px;
                                font-family: 'Arial';
                                color: black;
                                padding: 20px;  
                                border-radius: 10px;
                                text-align: center;
                            }
                        """)
        output = QLabel('Потрачено всего')
        output.setStyleSheet("""
                    QLabel {
                        font-size: 24px;
                        font-family: 'Arial';
                        color: black;
                        padding: 20px;  
                        border-radius: 10px;
                        text-align: center;
                    }
                """)
        layout_text = QHBoxLayout()
        layout_text.addWidget(input)
        layout_text.addWidget(output)

        layout_input = QHBoxLayout()
        self.all_input = QLabel()
        self.all_input.setStyleSheet("""
                    QLabel {
                        font-size: 24px;
                        font-family: 'Arial';
                        background-color: rgba(128, 128, 128, 150);
                        color: white;
                        padding: 20px;  
                        border-radius: 10px;
                        text-align: center;
                    }
                """)
        self.all_output = QLabel()
        self.all_output.setStyleSheet("""
                            QLabel {
                                font-size: 24px;
                                font-family: 'Arial';
                                background-color: rgba(128, 128, 128, 150);
                                color: white;
                                padding: 20px;  
                                border-radius: 10px;
                                text-align: center;
                            }
                        """)


        layout_input.addWidget(self.all_input)
        layout_input.addWidget(self.all_output)

        balance  = QLabel('Доступно на данный момент')
        balance.setStyleSheet("""
                            QLabel {
                                font-size: 24px;
                                font-family: 'Arial';
                                color: black;
                                padding: 20px;  
                                border-radius: 10px;
                                text-align: center;
                            }
                        """)
        self.balance_text = QLabel()
        self.balance_text.setStyleSheet("""
                            QLabel {
                                font-size: 24px;
                                font-family: 'Arial';
                                background-color: rgba(128, 128, 128, 150);
                                color: white;
                                padding: 20px;  
                                border-radius: 10px;
                                text-align: center;
                            }
                        """)

        layout.addLayout(layout_text)
        layout.addLayout(layout_input)
        layout.addWidget(balance)
        layout.addWidget(self.balance_text)
        self.setLayout(layout)
        self.update()

    def update(self):
        url = "https://open.er-api.com/v6/latest/USD"
        response = requests.get(url)
        data = response.json()
        rub = data['rates']['RUB']
        refill = get_refill()
        cost = get_cost()
        self.all_input.setText(f"{refill} ₽\n{round(refill/rub, 2)} $ ")
        self.all_output.setText(f"{cost} ₽\n{round(cost/rub, 2)} $")
        self.balance_text.setText(f"{refill - cost} ₽\n{round((refill - cost)/rub, 2)} $")










