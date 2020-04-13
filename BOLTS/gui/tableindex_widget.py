# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hugo/Documents/dev/bolts/BOLTS/output/freecad/BOLTS/gui/tableindex_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TableIndexWidget(object):
    def setupUi(self, TableIndexWidget):
        TableIndexWidget.setObjectName("TableIndexWidget")
        TableIndexWidget.resize(207, 68)
        self.horizontalLayout = QtWidgets.QHBoxLayout(TableIndexWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(TableIndexWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(TableIndexWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)

        self.retranslateUi(TableIndexWidget)
        QtCore.QMetaObject.connectSlotsByName(TableIndexWidget)

    def retranslateUi(self, TableIndexWidget):
        _translate = QtCore.QCoreApplication.translate
        TableIndexWidget.setWindowTitle(_translate("TableIndexWidget", "Form"))
        self.label.setText(_translate("TableIndexWidget", "TextLabel"))

