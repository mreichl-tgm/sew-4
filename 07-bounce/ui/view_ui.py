# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/data/OneDrive/_school/sew/Jg4/au07-bounce/ui/view.ui'
#
# Created: Mon Dec 12 18:39:47 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(748, 536)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.canvas = QtGui.QWidget(self.centralwidget)
        self.canvas.setObjectName("canvas")
        self.verticalLayout.addWidget(self.canvas)
        self.button_new = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_new.sizePolicy().hasHeightForWidth())
        self.button_new.setSizePolicy(sizePolicy)
        self.button_new.setObjectName("button_new")
        self.verticalLayout.addWidget(self.button_new)
        self.button_remove = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_remove.sizePolicy().hasHeightForWidth())
        self.button_remove.setSizePolicy(sizePolicy)
        self.button_remove.setObjectName("button_remove")
        self.verticalLayout.addWidget(self.button_remove)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 748, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Bounce Game", None, QtGui.QApplication.UnicodeUTF8))
        self.button_new.setText(QtGui.QApplication.translate("MainWindow", "New Point", None, QtGui.QApplication.UnicodeUTF8))
        self.button_remove.setText(QtGui.QApplication.translate("MainWindow", "Remove Point", None, QtGui.QApplication.UnicodeUTF8))

