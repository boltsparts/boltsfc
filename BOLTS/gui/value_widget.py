# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hugo/Documents/dev/bolts/BOLTS/output/freecad/BOLTS/gui/value_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ValueWidget(object):
    def setupUi(self, ValueWidget):
        ValueWidget.setObjectName("ValueWidget")
        ValueWidget.resize(150, 50)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ValueWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(ValueWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.valueEdit = QtWidgets.QLineEdit(ValueWidget)
        self.valueEdit.setObjectName("valueEdit")
        self.horizontalLayout.addWidget(self.valueEdit)

        self.retranslateUi(ValueWidget)
        QtCore.QMetaObject.connectSlotsByName(ValueWidget)

    def retranslateUi(self, ValueWidget):
        _translate = QtCore.QCoreApplication.translate
        ValueWidget.setWindowTitle(_translate("ValueWidget", "Form"))
        self.label.setText(_translate("ValueWidget", "TextLabel"))

