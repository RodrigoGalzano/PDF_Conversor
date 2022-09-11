import os
import sys
from pathlib import Path
import subprocess

from pdf2image import convert_from_path

import main
from qt_core import *
from gui.dialogs.ui_dialog import Ui_Dialog
from gui.windows.main_window.ui_main_window import UI_MainWindow
from gui.widgets.py_push_button import PyPushButton


def abreJanela(telaNova: UI_MainWindow, texto):
    telaNova.janela = QDialog()
    telaNova.ui_dialog = Ui_Dialog()
    telaNova.ui_dialog.setupUi(telaNova.janela)
    # self.btnOK.clicked.connect(Dialog.accept)
    telaNova.ui_dialog.btnOK.setStyleSheet(telaNova.ui_pages.btnSalvarPDF.styleSheet())
    telaNova.ui_dialog.label.setText(texto)

    telaNova.ui_dialog.btnFechar = PyPushButton(icon_path="x.svg")
    telaNova.ui_dialog.btnFechar.setMaximumSize(50, 20)
    telaNova.ui_dialog.btnFechar.setStyleSheet(telaNova.settings_btn.styleSheet())
    telaNova.ui_dialog.layoutTop.addWidget(telaNova.ui_dialog.btnFechar, 0, Qt.AlignRight|Qt.AlignTop)

    telaNova.janela.setStyleSheet(telaNova.left_menu.styleSheet())
    telaNova.janela.setWindowTitle('Informação')
    telaNova.ui_dialog.btnOK.clicked.connect(telaNova.janela.accept)
    telaNova.ui_dialog.btnFechar.clicked.connect(telaNova.janela.accept)
    telaNova.janela.setWindowFlag(Qt.FramelessWindowHint)

    telaNova.janela.exec_()
    print('teste')

def caminhoImage(nome_imagem):
    app_path = os.path.abspath(os.getcwd())
    folder = "gui/images/icons"
    path = os.path.join(app_path, folder)
    return os.path.normpath(os.path.join(path, nome_imagem))

class converter_PDF:
    def __init__(self,
                 caminhopdf,
                 caminhosave,
                 telaParent: UI_MainWindow
                 ):
        self.caminhopdf = caminhopdf
        self.caminhosave = caminhosave
        self.telaParent = telaParent

    def valida(self, tela):
        self.telaParent.ui_pages.lbl_msg_conversao.setStyleSheet("color: #F7122D; padding: 2px;")

        if self.caminhopdf == '':
            # abreJanela(tela,'Arquivo não informado.')
            self.telaParent.ui_pages.lbl_msg_conversao.setText("Arquivo não informado.")
            print('Arquivo não informado.')
            return False
        elif self.caminhosave == '':
            self.telaParent.ui_pages.lbl_msg_conversao.setText("Caimho para salvar não informado.")
            print('Caimho para salvar não informado.')
            return False
        else:
            if not os.path.isfile(self.caminhopdf):
                self.telaParent.ui_pages.lbl_msg_conversao.setText("Arquivo não encontrado.")
                print('Arquivo não encontrado.')
                return False

            if not os.path.isdir(self.caminhosave):
                self.telaParent.ui_pages.lbl_msg_conversao.setText("Não é um caminho válido.")
                print('Não é um caminho válido.')
                return False

        return True

    def converter_pdf_imagem(self, tipo, dpi=200, abre_pasta = False):
        if self.valida(self.telaParent):
            img = convert_from_path(self.caminhopdf, dpi=dpi,
                                    poppler_path=os.path.dirname(sys.executable) + '/poppler-0.68.0/bin')

            i = 1
            for imgs in img:
                imgs.save(self.caminhosave + '/' + Path(self.caminhopdf).stem + '_' + str(i) + '.' + tipo, tipo)
                i = i + 1

            if abre_pasta:
                os.startfile(self.caminhosave)

            return True
