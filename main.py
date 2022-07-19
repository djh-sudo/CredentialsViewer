from GUI.Mainwindow import Ui_MainWindow
import PyQt5.QtWidgets
import sys


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec())


