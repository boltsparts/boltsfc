# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hugo/Documents/dev/bolts/BOLTS/output/freecad/BOLTS/gui/bolts_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BoltsWidget(object):
    def setupUi(self, BoltsWidget):
        BoltsWidget.setObjectName("BoltsWidget")
        BoltsWidget.resize(333, 316)
        self.content = QtWidgets.QWidget()
        self.content.setEnabled(True)
        self.content.setObjectName("content")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.content)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.partsTree = QtWidgets.QTreeWidget(self.content)
        self.partsTree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.partsTree.setAutoExpandDelay(1)
        self.partsTree.setExpandsOnDoubleClick(False)
        self.partsTree.setColumnCount(2)
        self.partsTree.setObjectName("partsTree")
        self.partsTree.headerItem().setText(0, "Name")
        self.partsTree.header().setDefaultSectionSize(150)
        self.partsTree.header().setMinimumSectionSize(50)
        self.partsTree.header().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.partsTree)
        self.props = QtWidgets.QWidget(self.content)
        self.props.setMinimumSize(QtCore.QSize(0, 0))
        self.props.setObjectName("props")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.props)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.props_layout = QtWidgets.QVBoxLayout()
        self.props_layout.setObjectName("props_layout")
        self.verticalLayout_5.addLayout(self.props_layout)
        self.verticalLayout_2.addWidget(self.props)
        self.params = QtWidgets.QWidget(self.content)
        self.params.setObjectName("params")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.params)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.param_layout = QtWidgets.QVBoxLayout()
        self.param_layout.setObjectName("param_layout")
        self.verticalLayout_3.addLayout(self.param_layout)
        self.verticalLayout_2.addWidget(self.params)
        self.addButton = QtWidgets.QPushButton(self.content)
        self.addButton.setObjectName("addButton")
        self.verticalLayout_2.addWidget(self.addButton)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        BoltsWidget.setWidget(self.content)

        self.retranslateUi(BoltsWidget)
        QtCore.QMetaObject.connectSlotsByName(BoltsWidget)

    def retranslateUi(self, BoltsWidget):
        _translate = QtCore.QCoreApplication.translate
        BoltsWidget.setWindowTitle(_translate("BoltsWidget", "Standard Parts Selector"))
        self.partsTree.headerItem().setText(1, _translate("BoltsWidget", "Description"))
        self.addButton.setText(_translate("BoltsWidget", "Add Part"))

