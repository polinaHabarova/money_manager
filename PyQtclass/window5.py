from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class Window5(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel('Window5')
        layout.addWidget(label)
        self.setLayout(layout)