# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_files/Mywin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.screenheight = self.screenRect.height()
        self.screenwidth = self.screenRect.width()
        MainWindow.resize(self.screenwidth * 0.5, self.screenheight * 0.5)
        # MainWindow.resize(440, 420)
        self.Mainwidget = QtWidgets.QWidget(MainWindow)
        self.Mainwidget.setObjectName("Mainwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Mainwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.Mainwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.socket_tab = QtWidgets.QWidget()
        self.socket_tab.setObjectName("socket_tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.socket_tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.socket_graph = GraphicsLayoutWidget(self.socket_tab)
        self.socket_graph.setObjectName("socket_graph")
        self.horizontalLayout_3.addWidget(self.socket_graph)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.socket_tab)
        self.groupBox_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.groupBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(5, 6, 5, 0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(8)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.port_input = QtWidgets.QLineEdit(self.groupBox_2)
        self.port_input.setMinimumSize(QtCore.QSize(70, 0))
        self.port_input.setAlignment(QtCore.Qt.AlignCenter)
        self.port_input.setObjectName("port_input")
        self.gridLayout_2.addWidget(self.port_input, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.socket_mode = QtWidgets.QComboBox(self.groupBox_2)
        self.socket_mode.setMaxVisibleItems(0)
        self.socket_mode.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.socket_mode.setObjectName("socket_mode")
        self.gridLayout_2.addWidget(self.socket_mode, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setLineWidth(0)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.ip_com = QtWidgets.QComboBox(self.groupBox_2)
        self.ip_com.setMaxVisibleItems(5)
        self.ip_com.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.ip_com.setFrame(True)
        self.ip_com.setObjectName("ip_com")
        self.gridLayout_2.addWidget(self.ip_com, 3, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.socket_tab)
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.socket_switch = QtWidgets.QCheckBox(self.groupBox)
        self.socket_switch.setObjectName("socket_switch")
        self.gridLayout.addWidget(self.socket_switch, 0, 0, 1, 1)
        self.socket_paint_switch = QtWidgets.QCheckBox(self.groupBox)
        self.socket_paint_switch.setChecked(False)
        self.socket_paint_switch.setObjectName("socket_paint_switch")
        self.gridLayout.addWidget(self.socket_paint_switch, 1, 0, 1, 1)
        self.recv_data_btn = QtWidgets.QCheckBox(self.groupBox)
        self.recv_data_btn.setChecked(True)
        self.recv_data_btn.setObjectName("recv_data_btn")
        self.gridLayout.addWidget(self.recv_data_btn, 2, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.horizontalLayout_3.setStretch(0, 8)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.socket_recv_show = QtWidgets.QTextEdit(self.socket_tab)
        self.socket_recv_show.setObjectName("socket_recv_show")
        self.horizontalLayout_4.addWidget(self.socket_recv_show)
        self.groupBox_3 = QtWidgets.QGroupBox(self.socket_tab)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setContentsMargins(5, 6, 5, 5)
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.save_socket_data = QtWidgets.QPushButton(self.groupBox_3)
        self.save_socket_data.setObjectName("save_socket_data")
        self.gridLayout_3.addWidget(self.save_socket_data, 0, 0, 1, 1)
        self.clear_socket_data = QtWidgets.QPushButton(self.groupBox_3)
        self.clear_socket_data.setObjectName("clear_socket_data")
        self.gridLayout_3.addWidget(self.clear_socket_data, 1, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.groupBox_3)
        self.horizontalLayout_4.setStretch(0, 8)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.verticalLayout_7.setStretch(0, 8)
        self.verticalLayout_7.setStretch(1, 1)
        self.tabWidget.addTab(self.socket_tab, "")
        self.uart_tab = QtWidgets.QWidget()
        self.uart_tab.setObjectName("uart_tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.uart_tab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.serial_graph = GraphicsLayoutWidget(self.uart_tab)
        self.serial_graph.setObjectName("serial_graph")
        self.horizontalLayout.addWidget(self.serial_graph)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtWidgets.QLabel(self.uart_tab)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.uart_com = QtWidgets.QComboBox(self.uart_tab)
        self.uart_com.setObjectName("uart_com")
        self.gridLayout_5.addWidget(self.uart_com, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.uart_tab)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 2, 0, 1, 1)
        self.baud_boxcom = QtWidgets.QComboBox(self.uart_tab)
        self.baud_boxcom.setObjectName("baud_boxcom")
        self.gridLayout_5.addWidget(self.baud_boxcom, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.uart_config_btn = QtWidgets.QPushButton(self.uart_tab)
        self.uart_config_btn.setObjectName("uart_config_btn")
        self.gridLayout_4.addWidget(self.uart_config_btn, 0, 0, 1, 1)
        self.com_switch = QtWidgets.QCheckBox(self.uart_tab)
        self.com_switch.setObjectName("com_switch")
        self.gridLayout_4.addWidget(self.com_switch, 2, 0, 1, 1)
        self.uart_paint_switch = QtWidgets.QCheckBox(self.uart_tab)
        self.uart_paint_switch.setObjectName("uart_paint_switch")
        self.gridLayout_4.addWidget(self.uart_paint_switch, 3, 0, 1, 1)
        self.data_show_dialog = QtWidgets.QPushButton(self.uart_tab)
        self.data_show_dialog.setObjectName("data_show_dialog")
        self.gridLayout_4.addWidget(self.data_show_dialog, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 6)
        self.horizontalLayout.setStretch(1, 1)
        self.gridLayout_7.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.uart_recv_show = QtWidgets.QTextEdit(self.uart_tab)
        self.uart_recv_show.setObjectName("uart_recv_show")
        self.horizontalLayout_2.addWidget(self.uart_recv_show)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setVerticalSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.save_uart_data_btn = QtWidgets.QPushButton(self.uart_tab)
        self.save_uart_data_btn.setMinimumSize(QtCore.QSize(7, 0))
        self.save_uart_data_btn.setIconSize(QtCore.QSize(16, 16))
        self.save_uart_data_btn.setAutoExclusive(False)
        self.save_uart_data_btn.setDefault(False)
        self.save_uart_data_btn.setFlat(False)
        self.save_uart_data_btn.setObjectName("save_uart_data_btn")
        self.gridLayout_6.addWidget(self.save_uart_data_btn, 0, 0, 1, 1)
        self.clear_uart_data = QtWidgets.QPushButton(self.uart_tab)
        self.clear_uart_data.setObjectName("clear_uart_data")
        self.gridLayout_6.addWidget(self.clear_uart_data, 1, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_6)
        self.horizontalLayout_2.setStretch(0, 6)
        self.horizontalLayout_2.setStretch(1, 1)
        self.gridLayout_7.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_7.setRowStretch(0, 7)
        self.gridLayout_7.setRowStretch(1, 1)
        self.tabWidget.addTab(self.uart_tab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.Mainwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 440, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "端口"))
        self.label_3.setText(_translate("MainWindow", "ip选择"))
        self.label_5.setText(_translate("MainWindow", "模式选择"))
        self.socket_switch.setText(_translate("MainWindow", "打开连接"))
        self.socket_paint_switch.setText(_translate("MainWindow", "绘制图像"))
        self.recv_data_btn.setText(_translate("MainWindow", "接收数据"))
        self.save_socket_data.setText(_translate("MainWindow", "保存数据"))
        self.clear_socket_data.setText(_translate("MainWindow", "清空数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.socket_tab), _translate("MainWindow", "网络模式"))
        self.label_2.setText(_translate("MainWindow", "串口选择"))
        self.label.setText(_translate("MainWindow", "波特率"))
        self.uart_config_btn.setText(_translate("MainWindow", "更多配置"))
        self.com_switch.setText(_translate("MainWindow", "打开串口"))
        self.uart_paint_switch.setText(_translate("MainWindow", "绘制图像"))
        self.data_show_dialog.setText(_translate("MainWindow", "数据收发"))
        self.save_uart_data_btn.setText(_translate("MainWindow", "保存数据"))
        self.clear_uart_data.setText(_translate("MainWindow", "清空数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.uart_tab), _translate("MainWindow", "串口模式"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
from pyqtgraph import GraphicsLayoutWidget
