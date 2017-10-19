# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server.ui'
#
# Created: Sun Feb  5 19:52:16 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_view(object):
    def setupUi(self, view):
        view.setObjectName("view")
        view.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(view.sizePolicy().hasHeightForWidth())
        view.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(view)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtGui.QWidget(view)
        self.header.setMaximumSize(QtCore.QSize(16777215, 50))
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_port = QtGui.QLabel(self.header)
        self.label_port.setObjectName("label_port")
        self.horizontalLayout_2.addWidget(self.label_port)
        self.line_port = QtGui.QLineEdit(self.header)
        self.line_port.setObjectName("line_port")
        self.horizontalLayout_2.addWidget(self.line_port)
        self.btn_listen = QtGui.QPushButton(self.header)
        self.btn_listen.setObjectName("btn_listen")
        self.horizontalLayout_2.addWidget(self.btn_listen)
        self.list_clients = QtGui.QListWidget(self.header)
        self.list_clients.setMaximumSize(QtCore.QSize(16777215, 50))
        self.list_clients.setObjectName("list_clients")
        self.horizontalLayout_2.addWidget(self.list_clients)
        self.verticalLayout.addWidget(self.header)
        self.grid = QtGui.QGridLayout()
        self.grid.setObjectName("grid")
        self.verticalLayout.addLayout(self.grid)
        self.footer = QtGui.QWidget(view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.footer.sizePolicy().hasHeightForWidth())
        self.footer.setSizePolicy(sizePolicy)
        self.footer.setObjectName("footer")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.footer)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_shuffle = QtGui.QPushButton(self.footer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_shuffle.sizePolicy().hasHeightForWidth())
        self.btn_shuffle.setSizePolicy(sizePolicy)
        self.btn_shuffle.setObjectName("btn_shuffle")
        self.horizontalLayout_4.addWidget(self.btn_shuffle)
        self.verticalLayout.addWidget(self.footer)

        self.retranslateUi(view)
        QtCore.QMetaObject.connectSlotsByName(view)

    def retranslateUi(self, view):
        view.setWindowTitle(QtGui.QApplication.translate("view", "Server", None, QtGui.QApplication.UnicodeUTF8))
        self.label_port.setText(QtGui.QApplication.translate("view", "Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_listen.setText(QtGui.QApplication.translate("view", "Listen", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_shuffle.setText(QtGui.QApplication.translate("view", "Shuffe Map", None, QtGui.QApplication.UnicodeUTF8))

