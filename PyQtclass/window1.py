from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QTextBrowser

class Window1(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label_text = QLabel('Меню')
        label_text.setStyleSheet("""
                    QLabel {
                        background-image: url(image/title/forest.jpeg);
                        -webkit-background-clip: text;
                        color: transparent;
                        font-size: 170px;
                        font-family: 'Bungee', cursive;
                        padding-top: 20px;
                        text-align: center;
                    }
                """)
        layout.addWidget(label_text)

        input = QLabel('Получено всего')
        output = QLabel('Потрачено всего')
        layout_text = QHBoxLayout()
        layout_text.addWidget(input)
        layout_text.addWidget(output)

        layout_input = QHBoxLayout()
        self.all_input = QTextBrowser()
        self.all_output = QTextBrowser()

        layout_input.addWidget(self.all_input)
        layout_input.addWidget(self.all_output)

        balance  = QLabel('Доступно на данный момент')
        self.balance_text = QTextBrowser()

        layout.addLayout(layout_text)
        layout.addLayout(layout_input)
        layout.addWidget(balance)
        layout.addWidget(self.balance_text)
        self.setLayout(layout)
        self.set_text()
    def set_text(self):
        self.all_input.setPlainText('100')
        self.all_output.setPlainText('10')
        self.balance_text.setPlainText('1000')








