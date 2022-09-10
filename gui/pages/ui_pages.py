# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesaKYJEk.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSlider, QStackedWidget,
    QVBoxLayout, QWidget)
import r1_rc

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
        self.frame_Principal.setMinimumSize(QSize(500, 280))
        self.frame_Principal.setMaximumSize(QSize(500, 280))
        self.frame_Principal.setFrameShape(QFrame.StyledPanel)
        self.frame_Principal.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_Principal)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnCarregarPDF = QPushButton(self.frame_Principal)
        self.btnCarregarPDF.setObjectName(u"btnCarregarPDF")
        self.btnCarregarPDF.setMinimumSize(QSize(120, 50))
        self.btnCarregarPDF.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setBold(True)
        self.btnCarregarPDF.setFont(font)
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

        self.label = QLabel(self.frame_Principal)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 25))
        self.label.setMaximumSize(QSize(16777215, 25))
        self.label.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.btnSalvarPDF = QPushButton(self.frame_Principal)
        self.btnSalvarPDF.setObjectName(u"btnSalvarPDF")
        self.btnSalvarPDF.setMinimumSize(QSize(0, 50))
        self.btnSalvarPDF.setMaximumSize(QSize(16777215, 50))
        self.btnSalvarPDF.setFont(font)
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

        self.gridLayout.addWidget(self.btnSalvarPDF, 6, 0, 1, 2)

        self.edtCaminhoPDF = QLineEdit(self.frame_Principal)
        self.edtCaminhoPDF.setObjectName(u"edtCaminhoPDF")
        self.edtCaminhoPDF.setMinimumSize(QSize(0, 50))
        self.edtCaminhoPDF.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.edtCaminhoPDF.setFont(font1)
        self.edtCaminhoPDF.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(68, 71, 90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout.addWidget(self.edtCaminhoPDF, 2, 0, 1, 1)

        self.btnCarregarCaminhoSalvarPDF = QPushButton(self.frame_Principal)
        self.btnCarregarCaminhoSalvarPDF.setObjectName(u"btnCarregarCaminhoSalvarPDF")
        self.btnCarregarCaminhoSalvarPDF.setMinimumSize(QSize(0, 50))
        self.btnCarregarCaminhoSalvarPDF.setMaximumSize(QSize(16777215, 50))
        self.btnCarregarCaminhoSalvarPDF.setFont(font)
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

        self.edtCaminhoSalvarPDF = QLineEdit(self.frame_Principal)
        self.edtCaminhoSalvarPDF.setObjectName(u"edtCaminhoSalvarPDF")
        self.edtCaminhoSalvarPDF.setMinimumSize(QSize(0, 50))
        self.edtCaminhoSalvarPDF.setMaximumSize(QSize(16777215, 50))
        self.edtCaminhoSalvarPDF.setFont(font)
        self.edtCaminhoSalvarPDF.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(68, 71, 90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout.addWidget(self.edtCaminhoSalvarPDF, 4, 0, 1, 1)

        self.label_ola = QLabel(self.frame_Principal)
        self.label_ola.setObjectName(u"label_ola")
        self.label_ola.setMinimumSize(QSize(0, 25))
        self.label_ola.setMaximumSize(QSize(16777215, 25))
        self.label_ola.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_ola, 1, 0, 1, 1)

        self.checkBox = QCheckBox(self.frame_Principal)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 5, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)

        self.lbl_msg_conversao = QLabel(self.frame_Principal)
        self.lbl_msg_conversao.setObjectName(u"lbl_msg_conversao")
        self.lbl_msg_conversao.setStyleSheet(u"QLabel{\n"
"	padding: 2px;\n"
"	color: #F7122D\n"
"}")

        self.verticalLayout_4.addWidget(self.lbl_msg_conversao, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_Principal, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        application_pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_toggle_button = QFrame(self.page_2)
        self.frame_toggle_button.setObjectName(u"frame_toggle_button")
        self.frame_toggle_button.setMinimumSize(QSize(500, 250))
        self.frame_toggle_button.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle_button.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_toggle_button)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_page_2 = QVBoxLayout()
        self.verticalLayout_page_2.setObjectName(u"verticalLayout_page_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSlider = QSlider(self.frame_toggle_button)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimum(60)
        self.horizontalSlider.setMaximum(300)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 0, 2, 1, 1)

        self.label_2 = QLabel(self.frame_toggle_button)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1, Qt.AlignLeft)

        self.label_4 = QLabel(self.frame_toggle_button)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1, Qt.AlignLeft)

        self.comboBox = QComboBox(self.frame_toggle_button)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 30))
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#comboBox::drop-down{\n"
"	border: 0px;\n"
"}\n"
"\n"
"#comboBox::down-arrow{\n"
"   image: url(:/chevron-down.svg);\n"
"   width: 12px;\n"
"   height: 12px;\n"
"   margin-right: 15px;\n"
"}\n"
"\n"
"#comboBox:on{\n"
"   border: 4px solid #c2dbf;\n"
"}\n"
"\n"
"#comboBox QListView{\n"
"   font-size: 12px;\n"
"   border: 1px solid rgba(0,0,0, 10%);\n"
"   padding: 5px;\n"
"   background-color: #fff;\n"
"   outline: 0px;\n"
"}\n"
"\n"
"#comboBox QListView::item{\n"
"   padding-left: 10px;\n"
"   background-color: #fff;\n"
"   color: #000000\n"
"}\n"
"\n"
"#comboBox QListView::item:hover{\n"
"   background-color: #1e90ff;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.comboBox, 1, 2, 1, 1)


        self.verticalLayout_page_2.addLayout(self.gridLayout_2)

        self.chk_exemplo = QCheckBox(self.frame_toggle_button)
        self.chk_exemplo.setObjectName(u"chk_exemplo")
        self.chk_exemplo.setMinimumSize(QSize(0, 100))

        self.verticalLayout_page_2.addWidget(self.chk_exemplo, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_7.addLayout(self.verticalLayout_page_2)


        self.verticalLayout_2.addWidget(self.frame_toggle_button, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        application_pages.addWidget(self.page_2)
        self.page_circular_progress_bar = QWidget()
        self.page_circular_progress_bar.setObjectName(u"page_circular_progress_bar")
        self.verticalLayout_8 = QVBoxLayout(self.page_circular_progress_bar)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_circular_progress_bar = QFrame(self.page_circular_progress_bar)
        self.frame_circular_progress_bar.setObjectName(u"frame_circular_progress_bar")
        self.frame_circular_progress_bar.setMinimumSize(QSize(700, 300))
        self.frame_circular_progress_bar.setMaximumSize(QSize(700, 300))
        self.frame_circular_progress_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_circular_progress_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_circular_progress_bar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.grid_layout_layout_circular_progress_bar = QGridLayout()
        self.grid_layout_layout_circular_progress_bar.setObjectName(u"grid_layout_layout_circular_progress_bar")

        self.horizontalLayout_2.addLayout(self.grid_layout_layout_circular_progress_bar)


        self.verticalLayout_8.addWidget(self.frame_circular_progress_bar, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        application_pages.addWidget(self.page_circular_progress_bar)
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
        self.comboBoxTema.setFont(font)
        self.comboBoxTema.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#comboBoxTema::drop-down{\n"
"	border: 0px;\n"
"}\n"
"\n"
"#comboBoxTema::down-arrow{\n"
"   image: url(:/chevron-down.svg);\n"
"   width: 12px;\n"
"   height: 12px;\n"
"   margin-right: 15px;\n"
"}\n"
"\n"
"#comboBoxTema:on{\n"
"   border: 4px solid #c2dbf;\n"
"}\n"
"\n"
"#comboBoxTema QListView{\n"
"   font-size: 12px;\n"
"   border: 1px solid rgba(0,0,0, 10%);\n"
"   padding: 5px;\n"
"   background-color: #fff;\n"
"   outline: 0px;\n"
"}\n"
"\n"
"#comboBoxTema QListView::item{\n"
"   padding-left: 10px;\n"
"   background-color: #fff;\n"
"   color: #000000\n"
"}\n"
"\n"
"#comboBoxTema QListView::item:hover{\n"
"   background-color: #1e90ff;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.comboBoxTema.setInsertPolicy(QComboBox.InsertAtBottom)

        self.verticalLayout_5.addWidget(self.comboBoxTema)

        self.pshAplicarConfiguracoes = QPushButton(self.frame)
        self.pshAplicarConfiguracoes.setObjectName(u"pshAplicarConfiguracoes")
        self.pshAplicarConfiguracoes.setMinimumSize(QSize(100, 40))
        self.pshAplicarConfiguracoes.setMaximumSize(QSize(100, 40))
        self.pshAplicarConfiguracoes.setFont(font)
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

        application_pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(application_pages)
    # setupUi

    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(QCoreApplication.translate("application_pages", u"StackedWidget", None))
        self.btnCarregarPDF.setText(QCoreApplication.translate("application_pages", u"Carregar", None))
        self.label.setText(QCoreApplication.translate("application_pages", u"Caminho Salvar", None))
        self.btnSalvarPDF.setText(QCoreApplication.translate("application_pages", u"Converter PDF para PNG", None))
        self.edtCaminhoPDF.setPlaceholderText("")
        self.btnCarregarCaminhoSalvarPDF.setText(QCoreApplication.translate("application_pages", u"Carregar", None))
        self.label_ola.setText(QCoreApplication.translate("application_pages", u"Caminho Arquivo PDF", None))
        self.checkBox.setText(QCoreApplication.translate("application_pages", u"Abrir pasta ap\u00f3s convers\u00e3o?", None))
        self.lbl_msg_conversao.setText(QCoreApplication.translate("application_pages", u"lbl_msg_conversao", None))
        self.label_2.setText(QCoreApplication.translate("application_pages", u"Anima\u00e7\u00e3o", None))
        self.label_4.setText(QCoreApplication.translate("application_pages", u"Largura", None))
        self.chk_exemplo.setText(QCoreApplication.translate("application_pages", u"CheckBox", None))
        self.label_3.setText(QCoreApplication.translate("application_pages", u"Tema", None))
        self.comboBoxTema.setCurrentText("")
        self.comboBoxTema.setPlaceholderText(QCoreApplication.translate("application_pages", u"teste", None))
        self.pshAplicarConfiguracoes.setText(QCoreApplication.translate("application_pages", u"Aplicar", None))
    # retranslateUi

