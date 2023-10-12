# ----------------------------------------------------------- #
#       Обработчик стартового окна программы                  #
# ----------------------------------------------------------- #

# Импорты библиотек
from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import Qt

# Импорты модулей программы
from app.ui.py.about_developer_ui import Ui_AboutDeveloper


class AboutDeveloper(QDialog, Ui_AboutDeveloper):
    def __init__(self):
        '''
        Окно "Главное меню"
        '''
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.WindowMinimizeButtonHint | Qt.WindowType.Popup)
        self.pushButton.clicked.connect(self.close)
        self.show()