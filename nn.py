from PyQt6.QtWidgets import QApplication, QMessageBox

app = QApplication([])

# Создание QMessageBox
msg_box = QMessageBox()
msg_box.setIcon(QMessageBox.Icon.Information)
msg_box.setText("Это информационное сообщение.")
msg_box.setWindowTitle("Заголовок окна")
msg_box.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

# Отображение окна
result = msg_box.exec()

# Обработка результата
if result == QMessageBox.StandardButton.Ok:
    print("Пользователь нажал OK")
else:
    print("Пользователь нажал Cancel")

app.exec()