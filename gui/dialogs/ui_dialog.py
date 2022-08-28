# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogvBMBSv.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(527, 354)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 30)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.layoutTop = QHBoxLayout()
        self.layoutTop.setSpacing(0)
        self.layoutTop.setObjectName(u"layoutTop")

        self.verticalLayout_4.addLayout(self.layoutTop)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, -1, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 250))
        self.label.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.btnOK = QPushButton(self.widget)
        self.btnOK.setObjectName(u"btnOK")
        self.btnOK.setMinimumSize(QSize(70, 30))
        font = QFont()
        font.setBold(True)
        self.btnOK.setFont(font)
        self.btnOK.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 0, 127)	\n"
"}")

        self.verticalLayout_3.addWidget(self.btnOK, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"teste", None))
        self.btnOK.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

