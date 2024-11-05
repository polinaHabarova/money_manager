import sys
from PyQt6.QtWidgets import QApplication
from PyQtclass.main_window import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())