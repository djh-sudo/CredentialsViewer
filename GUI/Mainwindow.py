# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidget, QAbstractItemView, QTableWidgetItem
from setting import *
from rosource_rc import *
import SettingWindow
import re


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1289, 630)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tableWidget = QtWidgets.QTableWidget(self.splitter)
        self.tableWidget.setMinimumSize(QtCore.QSize(1200, 340))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.textEdit = QtWidgets.QTextEdit(self.splitter)
        self.textEdit.setMinimumSize(QtCore.QSize(1200, 210))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1289, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionCredentials_Decryption_Options = QtWidgets.QAction(MainWindow)
        self.actionCredentials_Decryption_Options.setObjectName("actionCredentials_Decryption_Options")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuOptions.addAction(self.actionCredentials_Decryption_Options)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        # ================================================
        self.setWindowIcon(QIcon(':/pic/title.png'))
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels([
            'Filename', 'Decrypted Size', 'Modified Time',
            'Persist', 'Entry Name', 'User Name', 'Password', 'Full Path', 'File Size'
        ])
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)

        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 400)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 200)
        self.tableWidget.setColumnWidth(5, 200)
        self.tableWidget.setColumnWidth(6, 200)
        self.tableWidget.setColumnWidth(7, 900)
        self.tableWidget.setColumnWidth(8, 200)

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)

        # ================================================
        self.form1 = QtWidgets.QMainWindow()
        self.setting_window = SettingWindow.Ui_MainWindow()
        self.setting_window.setWindowModality(Qt.ApplicationModal)
        self.setting_window.setWindowIcon(QIcon(':/pic/setting.png'))

        self.res = []

        self.InitShow()
        self.InitSignal()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CredentialViewer"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionCredentials_Decryption_Options.setText(_translate("MainWindow", "Credentials Decryption Options"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def InitShow(self):
        self.res = GetLocalCredential('')
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setSortingEnabled(False)
        self.ShowInfo()
        self.tableWidget.setSortingEnabled(True)

    def ShowInfo(self):
        if not self.res:
            return
        for enc, blob, _ in self.res:
            cur_row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(cur_row)
            self.tableWidget.setItem(cur_row, 0, QTableWidgetItem(enc._full_path.split('/')[-1].split('\\')[-1]))

            enc_sz = QTableWidgetItem()
            enc_sz.setData(QtCore.Qt.DisplayRole, blob.credSize)
            self.tableWidget.setItem(cur_row, 1, enc_sz)

            self.tableWidget.setItem(cur_row, 2, QTableWidgetItem(blob.LastWritten._file_time))
            self.tableWidget.setItem(cur_row, 3, QTableWidgetItem(enc.blob.szDescription))
            self.tableWidget.setItem(cur_row, 4, QTableWidgetItem(blob.TargetName))
            self.tableWidget.setItem(cur_row, 5, QTableWidgetItem(blob.UserName))
            self.tableWidget.setItem(cur_row, 6, QTableWidgetItem(blob.CredentialBlob))

            self.tableWidget.setItem(cur_row, 7, QTableWidgetItem(enc._full_path))

            block_sz = QTableWidgetItem()
            block_sz.setData(QtCore.Qt.DisplayRole, enc.blockSize)
            self.tableWidget.setItem(cur_row, 8, block_sz)

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

    def InitSignal(self):
        self.setting_window.signal.connect(self.Flush)
        self.actionCredentials_Decryption_Options.triggered.connect(self.OpenSettingWindow)
        self.tableWidget.itemClicked.connect(self.ShowContent)

    def OpenSettingWindow(self):
        self.setting_window.show()

    def Flush(self, psw: str):
        cred_files = Load('cred_files')
        sid_file = Load('sid_file')
        cache_sid_file = Load('cache_sid_file')
        if cred_files and sid_file and cache_sid_file:
            self.res = GetCredentials(psw, cred_files, sid_file, cache_sid_file)
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)
            self.tableWidget.setSortingEnabled(False)
            self.ShowInfo()
            self.tableWidget.setSortingEnabled(True)
        else:
            return

    def ShowContent(self, item):
        self.textEdit.clear()
        cur_row = item.row()
        if len(self.res[cur_row]) == 3:
            content = self.res[cur_row][2]
            iteration = len(content) // 32 + 1
            for it in range(iteration):
                text_list = re.findall(".{2}", content[it * 32:(it + 1) * 32])
                letter = ToASCII(text_list)
                new_text = " ".join(text_list)
                self.textEdit.append(new_text + '\t\t' + letter)

