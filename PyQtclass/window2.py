from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class Window2(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel('Window2')
        layout.addWidget(label)
        self.setLayout(layout)