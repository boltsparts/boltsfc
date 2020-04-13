# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hugo/Documents/dev/bolts/BOLTS/output/freecad/BOLTS/gui/bool_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BoolWidget(object):
    def setupUi(self, BoolWidget):
        BoolWidget.setObjectName("BoolWidget")
        BoolWidget.resize(114, 42)
        self.horizontalLayout = QtWidgets.QHBoxLayout(BoolWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(BoolWidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)

        self.retranslateUi(BoolWidget)
        QtCore.QMetaObject.connectSlotsByName(BoolWidget)

    def retranslateUi(self, BoolWidget):
        _translate = QtCore.QCoreApplication.translate
        BoolWidget.setWindowTitle(_translate("BoolWidget", "Form"))
        self.checkBox.setText(_translate("BoolWidget", "CheckBox"))

