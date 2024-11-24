from PyQt6.QtGui import QPainter, QFont, QPixmap, QPainterPath, QPen, QColor
from PyQt6.QtCore import Qt, QRect
from PyQt6.QtWidgets import QLabel, QWidget



class ImageTextLabel(QLabel):
    def __init__(self, text, image_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = text
        self.image_path = image_path
        self.setMinimumSize(400, 200)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        pixmap = QPixmap(self.image_path).scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding)

        font = QFont("Arial", 50, QFont.Weight.Bold)
        painter.setFont(font)

        path = QPainterPath()
        rect = QRect(0, 0, self.width(), self.height())
        path.addText(rect.center().x() - 100, rect.center().y() + 30, font, self.text)
        painter.setClipPath(path)
        painter.drawPixmap(rect, pixmap, pixmap.rect())

        painter.end()

class Line_widget(QWidget):
        def __init__(self):
            super().__init__()
            self.setMinimumSize(50, 50)

        def paintEvent(self, event):
           painter =  QPainter(self)
           painter.setPen(QPen(QColor(255, 234, 172), 5))
           painter.drawLine(0, 1, self.width(), 1)


