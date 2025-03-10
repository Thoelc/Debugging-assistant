# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_files/ConfigDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 159)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/image/avartar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.curve_num = QtWidgets.QSpinBox(Dialog)
        self.curve_num.setObjectName("curve_num")
        self.horizontalLayout.addWidget(self.curve_num)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.attention_range = QtWidgets.QLineEdit(Dialog)
        self.attention_range.setObjectName("attention_range")
        self.horizontalLayout_2.addWidget(self.attention_range)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ok = QtWidgets.QPushButton(Dialog)
        self.ok.setObjectName("ok")
        self.horizontalLayout_3.addWidget(self.ok)
        self.cancel = QtWidgets.QPushButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/image/关闭小.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel.setIcon(icon1)
        self.cancel.setCheckable(False)
        self.cancel.setAutoRepeat(False)
        self.cancel.setAutoExclusive(False)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_3.addWidget(self.cancel)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.cancel.clicked.connect(Dialog.reject)
        self.ok.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "曲线数量"))
        self.label_3.setText(_translate("Dialog", "默认区域大小 "))
        self.ok.setText(_translate("Dialog", "OK"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
import res_rc
