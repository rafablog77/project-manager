import os
import platform
import subprocess
from sys import argv

from PyQt6 import QtWidgets

from compiled_ui.mainwindow import Ui_MainWindow
from compiled_ui.add_program_dialog import Ui_Dialog


def open_file(path: str) -> None:
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


if __name__ == '__main__':

    class AddProgramDialog(QtWidgets.QDialog, Ui_Dialog):
        def __init__(self):
            super(AddProgramDialog, self).__init__()
            self.setupUi(self)



    class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
        def __init__(self, *args, obj=None, **kwargs):
            super(MainWindow, self).__init__(*args, **kwargs)
            self.setupUi(self)
            self.addProgram.clicked.connect(
                self.open_program_dialog
            )

        def open_program_dialog(self):
            dialog = AddProgramDialog()
            dialog.exec()



    app = QtWidgets.QApplication(argv)

    window = MainWindow()
    window.show()
    app.exec()