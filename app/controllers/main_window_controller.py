# ----------------------------------------------------------- #
#       Обработчик стартового окна программы                  #
# ----------------------------------------------------------- #

# Импорты библиотек
from PyQt6.QtWidgets import QMainWindow

# Импорты модулей программы
from app.ui.py.main_window_ui import Ui_MainWindow
from app.controllers.about_developer_controller import AboutDeveloper


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        '''
        Окно "Главное меню"
        '''
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        # self.pushButton_go_to_edit.clicked.connect(pass)
        self.pushButton_about_developer.clicked.connect(self.open_about_developer_dialog)
        self.show()

    def open_about_developer_dialog(self):
        '''
        Открытие модального окна "Новая игра"
        Связывание сигнала close() Главного меню и кнопки "Принять"
        в окне "Новая игра"
        '''
        self.about = AboutDeveloper()
        self.about.exec()
