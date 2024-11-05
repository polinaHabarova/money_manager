from PyQt6.QtWidgets import QWidget, QMainWindow, QStackedWidget, QHBoxLayout, QPushButton, QVBoxLayout
from PyQtclass.window1 import Window1
from PyQtclass.window2 import Window2
from PyQtclass.window3 import Window3
from PyQtclass.window4 import Window4
from PyQtclass.window5 import Window5


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Money Manager')
        self.stack_widget = QStackedWidget()

        self.Window1 = Window1()
        self.Window2 = Window2()
        self.Window3 = Window3()
        self.Window4 = Window4()
        self.Window5 = Window5()

        self.stack_widget.addWidget(self.Window1)
        self.stack_widget.addWidget(self.Window2)
        self.stack_widget.addWidget(self.Window3)
        self.stack_widget.addWidget(self.Window4)
        self.stack_widget.addWidget(self.Window5)

        button_layout = QHBoxLayout()
        self.buttons = []
        button_widget = QWidget()
        for i in range(5):
            button = QPushButton(f"Window{i + 1}")

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

            button.clicked.connect(lambda checked, index=i: self.switch_window(index))
            self.buttons.append(button)
            button_layout.addWidget(button)

        button_widget.setLayout(button_layout)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stack_widget)
        main_layout.addWidget(button_widget)

        center_widget = QWidget()
        center_widget.setLayout(main_layout)
        self.setCentralWidget(center_widget)

    def switch_window(self, index):
        self.stack_widget.setCurrentIndex(index)

