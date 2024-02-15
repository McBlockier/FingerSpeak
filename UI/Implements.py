from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QAbstractAnimation
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QMessageBox

class MethodsWindow:
    def on_start_button_clicked(self):
        pass
    def on_start_button_clicked_translate(self):
        pass
    def initializeComponents(self):
        pass
    def initializeVariables(self):
        pass
    def initializeStyles(self):
        pass

class ThreadWorker:
    def open_camera(self):
        pass


class hoverButton(QPushButton):
    def __init__(self, parent=None):
        QPushButton.__init__(self, parent)

        self.setMouseTracking(True)
        self.fuente = self.font()
        self.posicionX = int
        self.posicionY = int

    def enterEvent(self, event):
        self.posicionX = self.pos().x()
        self.posicionY = self.pos().y()

        self.animacionCursor = QPropertyAnimation(self, b"geometry")
        self.animacionCursor.setDuration(100)
        self.animacionCursor.setEndValue(QRect(self.posicionX - 15, self.posicionY - 6, 170, 38))
        self.animacionCursor.start(QAbstractAnimation.DeleteWhenStopped)

        self.fuente.setPointSize(11)
        self.setFont(self.fuente)

    def leaveEvent(self, event):
        self.fuente.setPointSize(10)
        self.setFont(self.fuente)

        self.animacionNoCursor = QPropertyAnimation(self, b"geometry")
        self.animacionNoCursor.setDuration(100)
        self.animacionNoCursor.setEndValue(QRect(self.posicionX, self.posicionY, 140, 28))
        self.animacionNoCursor.start(QAbstractAnimation.DeleteWhenStopped)