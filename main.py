import sys
import os
import rotinas as img

from qt_core import *

from gui.windows.main_window.ui_main_window import UI_MainWindow

from ui_splash_screen import Ui_SplashScreen
from gui.widgets.circular_progress import CircularProgress

# GOLBALS
counter = 0

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.ui.title.setText('PDF Conversor')
        self.ui.version.setText('v1.0.0')

        # Remove Title Bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Import Circular Progress
        self.progress = CircularProgress()
        self.progress.width = 270
        self.progress.height = 270
        self.progress.value = 0
        self.progress.progress_color = "#4674d9"
        self.progress.text_color = "#4674d9"
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.move(15, 15)
        self.progress.font_size = 40
        self.progress.add_shadow(True)
        self.progress.bg_color = QColor(68, 71, 90, 140)
        self.progress.setParent(self.ui.centralwidget)
        self.progress.show()


        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.setGraphicsEffect(self.shadow)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(25)

        self.show()

    def update(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.progress.set_value(counter)

        if counter >= 100:
            self.timer.stop()

            self.main = MainWindow()
            self.main.show()

            self.close()

        # Increase Counter
        counter += 1


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Curso de Python e Pyside6')
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # Toggle button
        self.ui.toggle_button.clicked.connect(self.toggle_button) #Esse parâmetro "self.toggle_button" é a função logo a baixo e não o botão
        self.ui.btn_1.clicked.connect(self.show_page_1)
        self.ui.btn_2.clicked.connect(self.btn_2Click)
        self.ui.btn_circular_progress_bar.clicked.connect(self.btn_circular_progress_bar_click)
        self.ui.settings_btn.clicked.connect(self.show_page_3)
        self.ui.ui_pages.btnCarregarPDF.clicked.connect(self.btnCarregarPDFClick)
        self.ui.ui_pages.btnCarregarCaminhoSalvarPDF.clicked.connect(self.btnCarregarCaminhoSalvarPDFClick)
        self.ui.ui_pages.btnSalvarPDF.clicked.connect(self.btnSalvarPDFClick)
        self.ui.ui_pages.pshAplicarConfiguracoes.clicked.connect(self.pshAplicarConfiguracoesClick)
        self.ui.btnFechar.clicked.connect(self.btnFecharClick)
        self.ui.btnMinimizar.clicked.connect(self.btnMinimizarClick)
        self.ui.btnMaximizar.clicked.connect(self.btnMaximizarClick)
        self.ui.ui_pages.horizontalSlider.valueChanged.connect(self.on_change_horizontalSlider)
        self.ui.ui_pages.comboBox.currentTextChanged.connect(self.on_combobox_changed)
        self.ui.slider_exemplo1.valueChanged.connect(self.slider_exemplo1_change_value)
        self.ui.slider_exemplo2.valueChanged.connect(self.slider_exemplo2_change_value)
        self.ui.slider_exemplo3.valueChanged.connect(self.slider_exemplo3_change_value)
        self.pshAplicarConfiguracoesClick()

        # Exemplo para transformar um componente em QSizeGrip em tempo de execução
        # QSizeGrip(self.ui.size_button)

        self.show()

    def slider_exemplo1_change_value(self, value):
        self.ui.progress_exemplo1.set_value(value)

    def slider_exemplo2_change_value(self, value):
        self.ui.progress_exemplo2.set_value(value)

    def slider_exemplo3_change_value(self, value):
        self.ui.progress_exemplo3.set_value(value)

    def on_combobox_changed(self, value):
        self.ui.toggle_exemplo.set_value(self.ui.ui_pages.horizontalSlider.value(), self.ui.ui_pages.comboBox.itemData(self.ui.ui_pages.comboBox.currentIndex()))

    def on_change_horizontalSlider(self, value):
        self.ui.toggle_exemplo.set_value(value, self.ui.ui_pages.comboBox.itemData(self.ui.ui_pages.comboBox.currentIndex()))

    def change_text(self):
        text = self.ui.ui_pages.lineEdit.text()
        new_text = "Olá, " + text
        self.ui.ui_pages.label_ola.setText(new_text)

    def openFileBrowser(self):
        result = QFileDialog.getOpenFileName(self, 'Carregar arquivo', 'D:/PDF_Teste', "PDF (*.PDF)")
        return result[0]

    def openDirectoryBrowser(self):
        result = QFileDialog.getExistingDirectory(self, 'Selecionar Pasta')
        return result

    def btnCarregarPDFClick(self):
        fname = self.openFileBrowser()
        self.ui.ui_pages.edtCaminhoPDF.setText(fname)

    def btnSalvarPDFClick(self):
        converte_pdf = img.converter_PDF(self.ui.ui_pages.edtCaminhoPDF.text(), self.ui.ui_pages.edtCaminhoSalvarPDF.text(), self.ui)
        if converte_pdf.converter_pdf_imagem('PNG', 200, self.ui.toggle_abrir_pasta.isChecked()):
            self.ui.ui_pages.lbl_msg_conversao.setStyleSheet("color: #4674d9; padding: 2px;")
            self.ui.ui_pages.lbl_msg_conversao.setText("Conversão realizada com sucesso.")

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

    def show_page_circular_progress_bar(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_circular_progress_bar)
        self.ui.btn_circular_progress_bar.set_active(True)

    def btn_circular_progress_bar_click(self):
        self.show_page_circular_progress_bar()

    def show_page_3(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
        self.ui.settings_btn.set_active(True)

    def btn_2Click(self):
        self.show_page_2()

    def btnFecharClick(self):
        self.close()

    def btnMinimizarClick(self):
        self.showMinimized()

    def btnMaximizarClick(self):
        global _old_size

        # CHECK EVENT
        if self.isMaximized():
            self.ui.changeUI(False)
            self.showNormal()
        else:
            _old_size = QSize(self.width(), self.height())
            self.ui.changeUI(True)
            self.showMaximized()

    def pshAplicarConfiguracoesClick(self):
        if self.ui.ui_pages.comboBoxTema.currentText() == "Black":
            self.ui.change_theme(cor_left_menu="#202020", cor_fundo_botoes_pages="#303030", cor_hover_botoes_pages="#454545" , cor_fundo_pages="#181818", cor_pressed_botoes_pages="#ffffff", cor_font_pressed_botoes_pages="#000000", cor_top_bottom_bar="#111111", cor_fundo_edit="#121212", cor_hover_btn_left_menu="#464646")
        elif self.ui.ui_pages.comboBoxTema.currentText() == "Purple":
            self.ui.change_theme(cor_left_menu="#44475a", cor_fundo_botoes_pages="rgb(67, 133, 200)", cor_hover_botoes_pages="rgb(85, 170, 255)", cor_fundo_pages="#282a36", cor_pressed_botoes_pages="rgb(255, 0, 127)", cor_font_pressed_botoes_pages="#ffffff", cor_top_bottom_bar="#21232d", cor_fundo_edit="rgb(68, 71, 90)", cor_hover_btn_left_menu="#4f5368")


    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()


    def mouseMoveEvent(self, event):
        #if not self.ui.size_grip.underMouse():
        if self.ui.window_top_frame_tela.underMouse():
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

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
    window = SplashScreen()
    sys.exit(app.exec())
