# ----------------------------------------------------------- #
#       Данный файл является точкой входа в программу.        #
# ----------------------------------------------------------- #

import sys
from PyQt6.QtWidgets import QApplication
from app.controllers.main_window_controller import MainWindow

# Создание экземпляра приложения QApplication
app = QApplication(sys.argv)

# Создание экземпляра стартового окна
window = MainWindow()

# Запуск главного цикла приложения
sys.exit(app.exec())
