# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pageskMioib.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_application_pages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(924, 541)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.page_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_Principal = QFrame(self.page_1)
        self.frame_Principal.setObjectName(u"frame_Principal")
        self.frame_Principal.setMinimumSize(QSize(500, 240))
        self.frame_Principal.setMaximumSize(QSize(500, 240))
        self.frame_Principal.setFrameShape(QFrame.StyledPanel)
        self.frame_Principal.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_Principal)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.edtCaminhoPDF = QLineEdit(self.frame_Principal)
        self.edtCaminhoPDF.setObjectName(u"edtCaminhoPDF")
        self.edtCaminhoPDF.setMinimumSize(QSize(0, 50))
        self.edtCaminhoPDF.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.edtCaminhoPDF.setFont(font)
        self.edtCaminhoPDF.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(68, 71, 90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout.addWidget(self.edtCaminhoPDF, 2, 0, 1, 1)

        self.btnCarregarPDF = QPushButton(self.frame_Principal)
        self.btnCarregarPDF.setObjectName(u"btnCarregarPDF")
        self.btnCarregarPDF.setMinimumSize(QSize(120, 50))
        self.btnCarregarPDF.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setBold(True)
        self.btnCarregarPDF.setFont(font1)
        self.btnCarregarPDF.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout.addWidget(self.btnCarregarPDF, 2, 1, 1, 1)

        self.label_ola = QLabel(self.frame_Principal)
        self.label_ola.setObjectName(u"label_ola")
        self.label_ola.setMinimumSize(QSize(0, 25))
        self.label_ola.setMaximumSize(QSize(16777215, 25))
        self.label_ola.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_ola, 1, 0, 1, 1)

        self.edtCaminhoSalvarPDF = QLineEdit(self.frame_Principal)
        self.edtCaminhoSalvarPDF.setObjectName(u"edtCaminhoSalvarPDF")
        self.edtCaminhoSalvarPDF.setMinimumSize(QSize(0, 50))
        self.edtCaminhoSalvarPDF.setMaximumSize(QSize(16777215, 50))
        self.edtCaminhoSalvarPDF.setFont(font1)
        self.edtCaminhoSalvarPDF.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(68, 71, 90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout.addWidget(self.edtCaminhoSalvarPDF, 4, 0, 1, 1)

        self.label = QLabel(self.frame_Principal)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 25))
        self.label.setMaximumSize(QSize(16777215, 25))
        self.label.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.btnCarregarCaminhoSalvarPDF = QPushButton(self.frame_Principal)
        self.btnCarregarCaminhoSalvarPDF.setObjectName(u"btnCarregarCaminhoSalvarPDF")
        self.btnCarregarCaminhoSalvarPDF.setMinimumSize(QSize(0, 50))
        self.btnCarregarCaminhoSalvarPDF.setMaximumSize(QSize(16777215, 50))
        self.btnCarregarCaminhoSalvarPDF.setFont(font1)
        self.btnCarregarCaminhoSalvarPDF.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout.addWidget(self.btnCarregarCaminhoSalvarPDF, 4, 1, 1, 1)

        self.btnSalvarPDF = QPushButton(self.frame_Principal)
        self.btnSalvarPDF.setObjectName(u"btnSalvarPDF")
        self.btnSalvarPDF.setMinimumSize(QSize(0, 50))
        self.btnSalvarPDF.setMaximumSize(QSize(16777215, 50))
        self.btnSalvarPDF.setFont(font1)
        self.btnSalvarPDF.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout.addWidget(self.btnSalvarPDF, 5, 0, 1, 2)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.frame_Principal, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        application_pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        application_pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.page_3)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 150))
        self.frame.setMaximumSize(QSize(500, 150))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(False)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.label_3)

        self.comboBoxTema = QComboBox(self.frame)
        self.comboBoxTema.setObjectName(u"comboBoxTema")
        self.comboBoxTema.setMinimumSize(QSize(350, 40))
        self.comboBoxTema.setMaximumSize(QSize(350, 40))
        self.comboBoxTema.setFont(font1)
        self.comboBoxTema.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.comboBoxTema.setInsertPolicy(QComboBox.InsertAtBottom)

        self.verticalLayout_5.addWidget(self.comboBoxTema)

        self.pshAplicarConfiguracoes = QPushButton(self.frame)
        self.pshAplicarConfiguracoes.setObjectName(u"pshAplicarConfiguracoes")
        self.pshAplicarConfiguracoes.setMinimumSize(QSize(100, 40))
        self.pshAplicarConfiguracoes.setMaximumSize(QSize(100, 40))
        self.pshAplicarConfiguracoes.setFont(font1)
        self.pshAplicarConfiguracoes.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_5.addWidget(self.pshAplicarConfiguracoes)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        application_pages.addWidget(self.page_3)

        self.retranslateUi(application_pages)

        application_pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(application_pages)
    # setupUi

    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(QCoreApplication.translate("application_pages", u"StackedWidget", None))
        self.edtCaminhoPDF.setPlaceholderText("")
        self.btnCarregarPDF.setText(QCoreApplication.translate("application_pages", u"Carregar", None))
        self.label_ola.setText(QCoreApplication.translate("application_pages", u"Caminho Arquivo PDF", None))
        self.label.setText(QCoreApplication.translate("application_pages", u"Caminho Salvar", None))
        self.btnCarregarCaminhoSalvarPDF.setText(QCoreApplication.translate("application_pages", u"Carregar", None))
        self.btnSalvarPDF.setText(QCoreApplication.translate("application_pages", u"Converter", None))
        self.label_2.setText(QCoreApplication.translate("application_pages", u"Pagina 2", None))
        self.label_3.setText(QCoreApplication.translate("application_pages", u"Tema", None))
        self.comboBoxTema.setCurrentText("")
        self.comboBoxTema.setPlaceholderText(QCoreApplication.translate("application_pages", u"teste", None))
        self.pshAplicarConfiguracoes.setText(QCoreApplication.translate("application_pages", u"Aplicar", None))
    # retranslateUi

