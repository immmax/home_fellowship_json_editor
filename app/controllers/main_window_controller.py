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
        self.pushButton_go_to_edit.clicked.connect(self.go_to_edit_view)
        self.pushButton_about_developer.clicked.connect(self.open_about_developer_dialog)
        self.show()

    def go_to_edit_view(self):
        """
        Переход к экрану редактирования JSON-файла
        """
        self.stackedWidget.setCurrentIndex(1)

    def open_about_developer_dialog(self):
        '''
        Открытие диалогового окна "О разработчике"
        '''
        self.about = AboutDeveloper()
        self.about.exec()
