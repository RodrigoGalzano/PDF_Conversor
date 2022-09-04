import os

from PySide6.QtGui import QPainter

from qt_core import *

class WinPushButton(QPushButton):
    def __init__(self,
                 text = "",
                 height = 40,
                 width = 45,
                 text_padding = 55,
                 text_color = "#c3ccdf",
                 icon_path = "",
                 icon_color = "#c3ccdf",
                 btn_color = "#44475a",
                 btn_hover = "#4f5368",
                 btn_pressed = "#282a36",
                 is_active = False,
                 ):
        super().__init__()

        # Set default parameters
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)

        self.setMaximumWidth(width)
        self.setMinimumWidth(width)

        # Custom parameters
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active

        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_pressed = self.btn_pressed,
            is_active = self.is_active
        )

    def set_active(self, is_active_menu):
        self.set_style(
            text_padding=self.text_padding,
            text_color=self.text_color,
            btn_color=self.btn_color,
            btn_pressed=self.btn_pressed,
            btn_hover=self.btn_hover,
            is_active=is_active_menu
        )

    def set_style(self,
                  text_padding = 55,
                  text_color = "#c3ccdf",
                  btn_color="#44475a",
                  btn_hover = "#4f5368",
                  btn_pressed = "#282a36",
                  btn_icon_pressed = "#282a36",
                  is_active = False
                  ):
        style = f"""
        QPushButton {{
            color: {text_color};
            background-color: {btn_color};
            border: nome;
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100px;
            height: 100px; 
        }}
        QPushButton:hover {{
            background-color: {btn_hover};   
        }}
        QPushButton:pressed {{
            background-color: {btn_pressed};   
            color: {btn_icon_pressed};   
        }}
        """

        self.setStyleSheet(style)

    def paintEvent(self, event):
        # Return default style
        QPushButton.paintEvent(self, event)

        #Painter
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)

        rect = QRect(0, 0, self.width(), self.height())

        self.draw_icon(qp, self.icon_path, rect, self.icon_color)

        qp.end()

    def draw_icon(self, qp, image, rect, color):
        # Format Path
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/icons"
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, image))

        # Draw icon
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()