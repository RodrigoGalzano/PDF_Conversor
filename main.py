import sys
import os
import rotinas as img

from qt_core import *

from gui.windows.main_window.ui_main_window import UI_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Curso de Python e Pyside6')

        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # Toggle button
        self.ui.toggle_button.clicked.connect(self.toggle_button) #Esse parâmetro "self.toggle_button" é a função logo a baixo e não o botão
        self.ui.btn_1.clicked.connect(self.show_page_1)
        self.ui.btn_2.clicked.connect(self.btn_2Click)
        self.ui.settings_btn.clicked.connect(self.show_page_3)
        self.ui.ui_pages.btnCarregarPDF.clicked.connect(self.btnCarregarPDFClick)
        self.ui.ui_pages.btnCarregarCaminhoSalvarPDF.clicked.connect(self.btnCarregarCaminhoSalvarPDFClick)
        self.ui.ui_pages.btnSalvarPDF.clicked.connect(self.btnSalvarPDFClick)
        self.ui.ui_pages.pshAplicarConfiguracoes.clicked.connect(self.pshAplicarConfiguracoesClick)
        self.pshAplicarConfiguracoesClick()
        self.show()

    def change_text(self):
        text = self.ui.ui_pages.lineEdit.text()
        new_text = "Olá, " + text
        self.ui.ui_pages.label_ola.setText(new_text)

    def openFileBrowser(self):
        result = QFileDialog.getOpenFileName(self, 'Carregar arquivo', '', "PDF (*.PDF)")
        return result[0]

    def openDirectoryBrowser(self):
        result = QFileDialog.getExistingDirectory(self, 'Selecionar Pasta')
        return result

    def btnCarregarPDFClick(self):
        fname = self.openFileBrowser()
        self.ui.ui_pages.edtCaminhoPDF.setText(fname)

    def btnSalvarPDFClick(self):
        converte_pdf = img.converter_PDF(self.ui.ui_pages.edtCaminhoPDF.text(), self.ui.ui_pages.edtCaminhoSalvarPDF.text(), self.ui)
        converte_pdf.converter_pdf_imagem('PNG', 200)

    def btnCarregarCaminhoSalvarPDFClick(self):
        fname = self.openDirectoryBrowser()
        self.ui.ui_pages.edtCaminhoSalvarPDF.setText(fname)

    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass

    def show_page_1(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        self.ui.btn_1.set_active(True)

    def show_page_2(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.btn_2.set_active(True)

    def show_page_3(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
        self.ui.settings_btn.set_active(True)

    def btn_2Click(self):
        self.show_page_2()

    def pshAplicarConfiguracoesClick(self):
        if self.ui.ui_pages.comboBoxTema.currentText() == "Black":
            self.ui.change_theme(cor_left_menu="#202020", cor_fundo_botoes_pages="#303030", cor_hover_botoes_pages="#454545" , cor_fundo_pages="#181818", cor_pressed_botoes_pages="#ffffff", cor_font_pressed_botoes_pages="#000000", cor_top_bottom_bar="#111111", cor_fundo_edit="#121212", cor_hover_btn_left_menu="#464646")
        elif self.ui.ui_pages.comboBoxTema.currentText() == "Purple":
            self.ui.change_theme(cor_left_menu="#44475a", cor_fundo_botoes_pages="rgb(67, 133, 200)", cor_hover_botoes_pages="rgb(85, 170, 255)", cor_fundo_pages="#282a36", cor_pressed_botoes_pages="rgb(255, 0, 127)", cor_font_pressed_botoes_pages="#ffffff", cor_top_bottom_bar="#21232d", cor_fundo_edit="rgb(68, 71, 90)", cor_hover_btn_left_menu="#4f5368")

    def toggle_button(self):
        # Get menu width
        menu_width = self.ui.left_menu.width()

        # Check with
        width = 50
        if menu_width == 50:
            width = 240

        # Start animation
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
