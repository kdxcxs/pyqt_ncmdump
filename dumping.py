# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dumping.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dumpingDialog(object):
    def setupUi(self, dumpingDialog):
        dumpingDialog.setObjectName("dumpingDialog")
        dumpingDialog.resize(300, 150)
        self.label = QtWidgets.QLabel(dumpingDialog)
        self.label.setGeometry(QtCore.QRect(75, 40, 150, 50))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(dumpingDialog)
        QtCore.QMetaObject.connectSlotsByName(dumpingDialog)

    def retranslateUi(self, dumpingDialog):
        _translate = QtCore.QCoreApplication.translate
        dumpingDialog.setWindowTitle(_translate("dumpingDialog", "转换中"))
        self.label.setText(_translate("dumpingDialog", "转换中\n"
"0/0"))
