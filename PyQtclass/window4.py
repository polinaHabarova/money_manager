from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class Window4(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel('Window4')
        layout.addWidget(label)
        self.setLayout(layout)