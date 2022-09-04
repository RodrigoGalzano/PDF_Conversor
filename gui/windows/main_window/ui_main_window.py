from qt_core import *
import os

from gui.pages.ui_pages import Ui_application_pages

from gui.widgets.py_push_button import PyPushButton
from gui.widgets.button_win_menu import WinPushButton
from gui.dialogs.ui_dialog import Ui_Dialog


class UI_MainWindow(object):
    def setup_ui(self, parent, cor_left_menu="#44475a"):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        self.cor_left_menu = "#44475a"
        self.cor_content = "#282a36"

        # SET INITIAL PARAMETERS
        # /////////////////////////////////////////////////////////////////
        parent.resize(1200, 720)
        parent.setMinimumSize(960, 540)

        # Frame Principal todos os outros estão dentro dele
        self.window_top_frame = QFrame()

        # LAYOUT Principal horizontal um frame a barra com o botão de fechar e o outro são os frame da aplicação
        self.window_top_layout = QVBoxLayout(self.window_top_frame)
        self.window_top_layout.setContentsMargins(0, 0, 0, 0)
        self.window_top_layout.setSpacing(0)

        # Frame barra com o botão de fechar
        self.window_top_frame_tela = QFrame()
        self.window_top_frame_tela.setStyleSheet('background-color: ' + self.cor_content)
        self.window_top_frame_tela.setMinimumHeight(25)
        self.window_top_frame_tela.setMaximumHeight(25)

        # Layout barra com o botão de fechar
        self.window_menu_layout_tela = QHBoxLayout(self.window_top_frame_tela)
        self.window_menu_layout_tela.setContentsMargins(0, 0, 0, 0)
        self.window_menu_layout_tela.setSpacing(0)

        self.btnMinimizar = WinPushButton(icon_path="icon_minimize.svg", height=self.window_top_frame_tela.height(), btn_color=self.cor_content)

        self.btnMaximizar = WinPushButton(icon_path="icon_maximize.svg", height=self.window_top_frame_tela.height(), btn_color=self.cor_content)

        self.btnFechar = WinPushButton(icon_path="icon_close.svg", height=self.window_top_frame_tela.height(), btn_color=self.cor_content)

        self.estilo_win_psh_button_inicial = self.btnFechar.styleSheet()

        self.windows_menu_spacer = QSpacerItem(50, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.window_menu_layout_tela.addItem(self.windows_menu_spacer)
        self.window_menu_layout_tela.addWidget(self.btnMinimizar, 0, Qt.AlignRight | Qt.AlignTop)
        self.window_menu_layout_tela.addWidget(self.btnMaximizar, 0, Qt.AlignRight | Qt.AlignTop)
        self.window_menu_layout_tela.addWidget(self.btnFechar, 0, Qt.AlignRight | Qt.AlignTop)

        # CREATE CENTRAL WIDGET
        # /////////////////////////////////////////////////////////////////
        self.central_frame = QFrame()

        # ADD frame do botão fechar e frame da aplicação
        self.window_top_layout.addWidget(self.window_top_frame_tela)
        self.window_top_layout.addWidget(self.central_frame)

        # CREATE MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # LEFT MENU
        # /////////////////////////////////////////////////////////////////
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet('background-color: ' + self.cor_left_menu)
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)

        # LEFT MENU LAYOUT
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)

        # TOP FRAME MENU
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(40)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")

        # TOP FRAME LAYOUT
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_layout.setSpacing(0)

        # TOP BTNS
        self.toggle_button = PyPushButton(text='Ocultar menu', icon_path="icon_menu.svg")
        self.btn_1 = PyPushButton(text='Página Inicial', is_active=True, icon_path="icon_home.svg")
        self.btn_2 = PyPushButton(text='Página 2', icon_path="icon_widgets.svg")

        # ADD BTNS TO LAYOUT
        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.btn_1)
        self.left_menu_top_layout.addWidget(self.btn_2)

        # MENU SPACER
        # /////////////////////////////////////////////////////////////////
        self.left_menu_spacer = QSpacerItem(20,20,QSizePolicy.Minimum,QSizePolicy.Expanding)

        # BOTTOM FRAME MENU
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(40)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")

        # BOTTOM FRAME LAYOUT
        # /////////////////////////////////////////////////////////////////
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bottom_layout.setSpacing(0)

        # BOTTOM BTNS
        self.settings_btn = PyPushButton(btn_color=cor_left_menu,text='Configurações', icon_path="icon_settings.svg")

        # ADD BTNS TO LAYOUT
        self.left_menu_bottom_layout.addWidget(self.settings_btn)

        # LABEL VERSION
        self.left_menu_label_version = QLabel("v1.0.0")
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMinimumHeight(30)
        self.left_menu_label_version.setMaximumHeight(30)
        self.left_menu_label_version.setStyleSheet("color: #c3ccdf")

        # ADD TO LAYOUT
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)

        # CONTENT
        self.content = QFrame()
        self.content.setStyleSheet("background-color: " + self.cor_content)

        # CONTENT LAYOUT
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # TOP BAR
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6277a4")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10, 0, 10, 0)

        # TOP BAR 2
        self.top_bar2 = QFrame()
        self.top_bar2.setMinimumHeight(30)
        self.top_bar2.setMaximumHeight(30)
        self.top_bar2.setStyleSheet("background-color: red")
        self.top_bar_layout2 = QHBoxLayout(self.top_bar2)
        self.top_bar_layout2.setContentsMargins(10, 0, 10, 0)

        # LEFT LABEL
        self.top_label_left = QLabel("Essa é minha primeira aplicação com PySide6")

        # TOP SPACER
        self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # RIGHT LABEL
        self.top_label_right = QLabel("| PÁGINA INICIAL")
        self.top_label_right.setStyleSheet("font: 700 9pt 'Sergoe UI'")

        # ADD TO LAYOUT
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)

        # APPLICATION PAGES
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2")
        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(self.pages)
        self.ui_pages.comboBoxTema.addItem("Black", "", "")
        self.ui_pages.comboBoxTema.addItem("Purple", "", "")
        self.ui_pages.comboBoxTema.setCurrentIndex(0)
        self.pages.setCurrentWidget(self.ui_pages.page_1)

        # TOP BAR
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6277a4")

        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10, 0, 10, 0)

        # LEFT LABEL
        self.bottom_label_left = QLabel("Criado por: Rodrigo Galzano")

        # TOP SPACER
        self.bottom_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # RIGHT LABEL
        # self.bottom_label_right = QLabel("@ 2022")

        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/icons"
        path = os.path.join(app_path, folder)
        path = os.path.normpath(os.path.join(path, 'ressize.svg'))

        self.size_grip = QSizeGrip(self.bottom_bar)

        # ADD TO LAYOUT
        self.bottom_bar_layout.addWidget(self.bottom_label_left)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.size_grip)

        # ADD TO C0NTENT LAYOUT
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        # ADD WIDGETS TO APP
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.window_top_frame)

        #GET styleSheet Botoes
        self.estilo_botoes_incial = self.ui_pages.btnSalvarPDF.styleSheet()
        self.estilo_combo_incial = self.ui_pages.comboBoxTema.styleSheet()
        self.estilo_edit_inicial = self.ui_pages.edtCaminhoPDF.styleSheet()

    def changeUI(self, bMaximizado):
        if bMaximizado:
            self.btnMaximizar.icon_path = "icon_restore.svg"
        else:
            self.btnMaximizar.icon_path = "icon_maximize.svg"



    def change_theme(self, cor_left_menu, cor_fundo_botoes_pages, cor_hover_botoes_pages, cor_fundo_pages, cor_pressed_botoes_pages , cor_font_pressed_botoes_pages, cor_top_bottom_bar, cor_fundo_edit, cor_hover_btn_left_menu):
        self.left_menu.setStyleSheet('background-color: ' + cor_left_menu)
        self.cor_left_menu = cor_left_menu
        self.content.setStyleSheet("background-color: " + cor_fundo_pages)
        self.cor_content = cor_fundo_pages
        self.window_top_frame_tela.setStyleSheet('background-color: ' + cor_top_bottom_bar)
        self.top_bar.setStyleSheet("background-color: " + cor_top_bottom_bar + "; color: #6277a4")
        self.bottom_bar.setStyleSheet("background-color: " + cor_top_bottom_bar + "; color: #6277a4")

        for btn in self.left_menu.findChildren(PyPushButton):
            try:
                btn.btn_color = cor_left_menu
                btn.btn_hover = cor_hover_btn_left_menu
                btn.btn_pressed = cor_fundo_pages
                btn.set_style(btn_color=cor_left_menu, btn_hover=cor_hover_btn_left_menu, btn_pressed=self.cor_content)
            except:
                pass

        style_botoes_novo = f"""
        QPushButton {{
            background-color: {cor_fundo_botoes_pages};
        }}
        QPushButton:hover {{
            background-color: {cor_hover_botoes_pages};   
        }}
        QPushButton:pressed {{
            background-color: {cor_pressed_botoes_pages};
            color: {cor_font_pressed_botoes_pages} 
        }}
        """

        for btn in self.pages.findChildren(QPushButton):
            try:
                btn.setStyleSheet(self.estilo_botoes_incial + style_botoes_novo)
            except:
                pass

        style_combo_novo = f"""
        QComboBox {{
            background-color: {cor_fundo_botoes_pages};
        }}
        """

        for btn in self.pages.findChildren(QComboBox):
            try:
                btn.setStyleSheet(self.estilo_combo_incial + style_combo_novo)
            except:
                pass

        style_edit_novo = f"""
        QLineEdit {{
            background-color: {cor_fundo_edit};
        }}
        """

        for btn in self.pages.findChildren(QLineEdit):
            try:
                btn.setStyleSheet(self.estilo_edit_inicial + style_edit_novo)
            except:
                pass

        style_win_psh_novo = f"""
        QPushButton {{
            background-color: {cor_top_bottom_bar};
        }}
        """

        for btn in self.window_top_frame.findChildren(WinPushButton):
            try:
                btn.btn_color = cor_left_menu
                btn.btn_hover = cor_hover_btn_left_menu
                btn.btn_pressed = cor_fundo_pages
                btn.set_style(btn_color=cor_top_bottom_bar, btn_hover=cor_hover_btn_left_menu, btn_pressed=cor_pressed_botoes_pages, btn_icon_pressed=cor_pressed_botoes_pages)
            except:
                pass



