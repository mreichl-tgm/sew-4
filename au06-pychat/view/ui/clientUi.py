# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/data/OneDrive/_school/sew/Jg4/au06-pychat/view/ui/client.ui'
#
# Created: Fri Dec  2 18:01:49 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.msgbox = QtGui.QLineEdit(self.centralwidget)
        self.msgbox.setObjectName("msgbox")
        self.horizontalLayout.addWidget(self.msgbox)
        self.bsend = QtGui.QPushButton(self.centralwidget)
        self.bsend.setObjectName("bsend")
        self.horizontalLayout.addWidget(self.bsend)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.chat = QtGui.QTextBrowser(self.centralwidget)
        self.chat.setObjectName("chat")
        self.verticalLayout_2.addWidget(self.chat)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.bsend, self.msgbox)
        MainWindow.setTabOrder(self.msgbox, self.chat)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Chat - Client", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Message:", None, QtGui.QApplication.UnicodeUTF8))
        self.bsend.setText(QtGui.QApplication.translate("MainWindow", "Send", None, QtGui.QApplication.UnicodeUTF8))

