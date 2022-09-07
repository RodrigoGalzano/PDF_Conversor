from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtGui import QFont
from PySide6.QtWidgets import *

class PyToggle(QCheckBox):
    def __init__(self, 
                 width = 60,
                 bg_color = "#777",
                 circle_color = "#DDD",
                 active_color = "#00bcff",
                 animation_curve = QEasingCurve.OutBounce
    ):
        QCheckBox.__init__(self, )

        # Set Default Parameters
        self.width = width
        self.setFixedSize(width, 28)
        self.setCursor(Qt.PointingHandCursor)

        # Colors
        self._bg_color = bg_color
        self._circle_color = circle_color
        self._active_color = active_color

        # Create Animation
        self._circle_position = 3
        self.animation = QPropertyAnimation(self, b"circle_position", self)
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(500)

        self.stateChanged.connect(self.start_transition)

    @Property(float)
    def circle_position(self):
        return self._circle_position

    @circle_position.setter
    def circle_position(self, pos):
        self._circle_position = pos
        self.update()

    def start_transition(self, value):
        self.animation.stop()

        if value:
            self.animation.setEndValue(self.width - 26)
        else:
            self.animation.setEndValue(3)

        self.animation.start()

        # print(f"Stats: {self.isChecked()}")

    def set_value(self, width, tipo_animacao : QEasingCurve):
        self.width = width
        self.animation.setEasingCurve(tipo_animacao)
        self.repaint()

    # SET NEW HIT AREA
    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)

    def paintEvent(self, e):
        width_texto = self.fontMetrics().boundingRect(self.text()).width()

        self.setFixedSize(self.width + width_texto + 10, 28)

        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        p.drawText(QPoint(66, 20), self.text())

        p.setPen(Qt.NoPen)

        tamanho_retangulo = self.width

        # DRAW RECTANGLE
        rect = QRect(0, 0, tamanho_retangulo, self.height())

        if not self.isChecked():
            # DRAW BG
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)

            # DRAW CIRCLE
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position, 3, 22, 22)
        else:
            # DRAW BG
            p.setBrush(QColor(self._active_color))
            p.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)

            # DRAW CIRCLE
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position, 3, 22, 22)

        p.end()
