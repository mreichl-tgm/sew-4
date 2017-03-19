# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sun Mar 19 18:46:27 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.feed = QtGui.QTextBrowser(self.centralwidget)
        self.feed.setObjectName("feed")
        self.gridLayout_2.addWidget(self.feed, 0, 1, 1, 1)
        self.publishers = QtGui.QTreeWidget(self.centralwidget)
        self.publishers.setObjectName("publishers")
        self.publishers.headerItem().setText(0, "Publishers")
        self.gridLayout_2.addWidget(self.publishers, 0, 0, 1, 1)
        self.subscribers = QtGui.QTreeWidget(self.centralwidget)
        self.subscribers.setObjectName("subscribers")
        self.subscribers.headerItem().setText(0, "Subscribers")
        self.gridLayout_2.addWidget(self.subscribers, 1, 0, 1, 1)
        self.inputwidget = QtGui.QVBoxLayout()
        self.inputwidget.setObjectName("inputwidget")
        self.input_label = QtGui.QLabel(self.centralwidget)
        self.input_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input_label.setAutoFillBackground(False)
        self.input_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.input_label.setObjectName("input_label")
        self.inputwidget.addWidget(self.input_label)
        self.input = QtGui.QTextEdit(self.centralwidget)
        self.input.setObjectName("input")
        self.inputwidget.addWidget(self.input)
        self.buttons = QtGui.QHBoxLayout()
        self.buttons.setObjectName("buttons")
        self.update_button = QtGui.QPushButton(self.centralwidget)
        self.update_button.setObjectName("update_button")
        self.buttons.addWidget(self.update_button)
        self.send_button = QtGui.QPushButton(self.centralwidget)
        self.send_button.setObjectName("send_button")
        self.buttons.addWidget(self.send_button)
        self.quit_button = QtGui.QPushButton(self.centralwidget)
        self.quit_button.setObjectName("quit_button")
        self.buttons.addWidget(self.quit_button)
        self.inputwidget.addLayout(self.buttons)
        self.gridLayout_2.addLayout(self.inputwidget, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.quit_button, QtCore.SIGNAL("clicked()"), MainWindow.close)
        QtCore.QObject.connect(self.send_button, QtCore.SIGNAL("clicked()"), self.input.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.input_label.setText(QtGui.QApplication.translate("MainWindow", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.update_button.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.send_button.setText(QtGui.QApplication.translate("MainWindow", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.quit_button.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))

