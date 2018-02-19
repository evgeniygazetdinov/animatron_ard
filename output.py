# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(549, 330)
        self.obtain_value = QtGui.QPushButton(Dialog)
        self.obtain_value.setGeometry(QtCore.QRect(440, 100, 91, 41))
        self.obtain_value.setCheckable(True)
        self.obtain_value.setObjectName(_fromUtf8("obtain_value"))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(350, 250, 181, 31))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(40, 170, 251, 16))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtGui.QProgressBar.BottomToTop)
        self.progressBar.setFormat(_fromUtf8(""))
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.progressBar_2 = QtGui.QProgressBar(Dialog)
        self.progressBar_2.setGeometry(QtCore.QRect(40, 220, 251, 16))
        self.progressBar_2.setProperty("value", 100)
        self.progressBar_2.setFormat(_fromUtf8(""))
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.play = QtGui.QPushButton(Dialog)
        self.play.setGeometry(QtCore.QRect(40, 100, 91, 51))
        self.play.setObjectName(_fromUtf8("play"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(250, 20, 281, 71))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 279, 69))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.play_2 = QtGui.QPushButton(Dialog)
        self.play_2.setGeometry(QtCore.QRect(150, 100, 91, 51))
        self.play_2.setObjectName(_fromUtf8("play_2"))
        self.commandLinkButton = QtGui.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(20, 270, 175, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.obtain_value.setText(_translate("Dialog", "add", None))
        self.play.setText(_translate("Dialog", "play", None))
        self.play_2.setText(_translate("Dialog", "stop", None))
        self.commandLinkButton.setText(_translate("Dialog", "CommandLinkButton", None))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_Dialog()
    sys.exit(app.exec_())