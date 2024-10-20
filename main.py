import os
import platform
import subprocess
from sys import argv

from PyQt6 import QtWidgets

from mainwindow import Ui_MainWindow

from PyQt6.QtWidgets import QComboBox, QPushButton, QListWidget


def open_file(path: str) -> None:
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


if __name__ == '__main__':
    class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
        def __init__(self, *args, obj=None, **kwargs):
            super(MainWindow, self).__init__(*args, **kwargs)
            self.setupUi(self)


    app = QtWidgets.QApplication(argv)

    window = MainWindow()
    window.show()
    app.exec()