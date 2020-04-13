# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hugo/Documents/dev/bolts/BOLTS/output/freecad/BOLTS/gui/property_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PropertyWidget(object):
    def setupUi(self, PropertyWidget):
        PropertyWidget.setObjectName("PropertyWidget")
        PropertyWidget.resize(152, 35)
        self.horizontalLayout = QtWidgets.QHBoxLayout(PropertyWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.prop = QtWidgets.QLabel(PropertyWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prop.sizePolicy().hasHeightForWidth())
        self.prop.setSizePolicy(sizePolicy)
        self.prop.setObjectName("prop")
        self.horizontalLayout.addWidget(self.prop)
        self.value = QtWidgets.QLabel(PropertyWidget)
        self.value.setWordWrap(True)
        self.value.setObjectName("value")
        self.horizontalLayout.addWidget(self.value)

        self.retranslateUi(PropertyWidget)
        QtCore.QMetaObject.connectSlotsByName(PropertyWidget)

    def retranslateUi(self, PropertyWidget):
        _translate = QtCore.QCoreApplication.translate
        PropertyWidget.setWindowTitle(_translate("PropertyWidget", "Form"))
        self.prop.setText(_translate("PropertyWidget", "TextLabel"))
        self.value.setText(_translate("PropertyWidget", "TextLabel"))

