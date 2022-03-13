# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Mega_Mike\Desktop\layout-main\design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Weights(object):
    def setupUi(self, Weights):
        Weights.setObjectName("Weights")
        Weights.resize(378, 458)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Weights.sizePolicy().hasHeightForWidth())
        Weights.setSizePolicy(sizePolicy)
        Weights.setMinimumSize(QtCore.QSize(378, 458))
        Weights.setMaximumSize(QtCore.QSize(378, 458))
        Weights.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(Weights)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(350, 350))
        self.centralwidget.setMaximumSize(QtCore.QSize(400, 500))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayoutPortsMain = QtWidgets.QHBoxLayout()
        self.horizontalLayoutPortsMain.setObjectName("horizontalLayoutPortsMain")
        self.settingsButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsButton.sizePolicy().hasHeightForWidth())
        self.settingsButton.setSizePolicy(sizePolicy)
        self.settingsButton.setMinimumSize(QtCore.QSize(10, 20))
        self.settingsButton.setMaximumSize(QtCore.QSize(25, 25))
        self.settingsButton.setBaseSize(QtCore.QSize(20, 20))
        self.settingsButton.setStyleSheet("image: url(:/images/images/settings.png);")
        self.settingsButton.setText("")
        self.settingsButton.setObjectName("settingsButton")
        self.horizontalLayoutPortsMain.addWidget(self.settingsButton)
        self.labelPort = QtWidgets.QLabel(self.centralwidget)
        self.labelPort.setMaximumSize(QtCore.QSize(40, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.labelPort.setFont(font)
        self.labelPort.setObjectName("labelPort")
        self.horizontalLayoutPortsMain.addWidget(self.labelPort)
        self.selectionWindow = QtWidgets.QComboBox(self.centralwidget)
        self.selectionWindow.setObjectName("selectionWindow")
        self.horizontalLayoutPortsMain.addWidget(self.selectionWindow)
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.connectButton.setFont(font)
        self.connectButton.setStyleSheet("image: url(:/images/images/refresh.png);")
        self.connectButton.setText("")
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayoutPortsMain.addWidget(self.connectButton)
        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.confirmButton.setStyleSheet("image: url(:/images/images/connect.png);")
        self.confirmButton.setText("")
        self.confirmButton.setObjectName("confirmButton")
        self.horizontalLayoutPortsMain.addWidget(self.confirmButton)
        self.disconnectButton = QtWidgets.QPushButton(self.centralwidget)
        self.disconnectButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.disconnectButton.setStyleSheet("image: url(:/images/images/disconnect.png);")
        self.disconnectButton.setText("")
        self.disconnectButton.setObjectName("disconnectButton")
        self.horizontalLayoutPortsMain.addWidget(self.disconnectButton)
        self.verticalLayout.addLayout(self.horizontalLayoutPortsMain)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.scrollArea.setPalette(palette)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 339, 192))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.scrollAreaWidgetContents_6.setPalette(palette)
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.textShow = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.textShow.setEnabled(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.textShow.setPalette(palette)
        self.textShow.setStyleSheet("background-color: white;")
        self.textShow.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textShow.setText("")
        self.textShow.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.textShow.setObjectName("textShow")
        self.verticalLayout_6.addWidget(self.textShow)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_6)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayoutMain = QtWidgets.QVBoxLayout()
        self.verticalLayoutMain.setObjectName("verticalLayoutMain")
        self.cleanButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cleanButton.setFont(font)
        self.cleanButton.setObjectName("cleanButton")
        self.verticalLayoutMain.addWidget(self.cleanButton)
        self.buttons = QtWidgets.QGridLayout()
        self.buttons.setObjectName("buttons")
        self.weighButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weighButton.sizePolicy().hasHeightForWidth())
        self.weighButton.setSizePolicy(sizePolicy)
        self.weighButton.setMinimumSize(QtCore.QSize(150, 70))
        self.weighButton.setBaseSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.weighButton.setFont(font)
        self.weighButton.setStyleSheet("QPushButton{\n"
"image: url(:/images/images/weight.png);\n"
"}")
        self.weighButton.setText("")
        self.weighButton.setIconSize(QtCore.QSize(150, 50))
        self.weighButton.setObjectName("weighButton")
        self.buttons.addWidget(self.weighButton, 0, 0, 1, 1)
        self.calibButton = QtWidgets.QPushButton(self.centralwidget)
        self.calibButton.setMinimumSize(QtCore.QSize(150, 70))
        self.calibButton.setStyleSheet("QPushButton{\n"
"image: url(:/images/images/calib.png);\n"
"}")
        self.calibButton.setText("")
        self.calibButton.setObjectName("calibButton")
        self.buttons.addWidget(self.calibButton, 0, 1, 1, 1)
        self.scanButton = QtWidgets.QPushButton(self.centralwidget)
        self.scanButton.setMinimumSize(QtCore.QSize(150, 70))
        self.scanButton.setStyleSheet("QPushButton{\n"
"image: url(:/images/images/scan.png);\n"
"}")
        self.scanButton.setText("")
        self.scanButton.setObjectName("scanButton")
        self.buttons.addWidget(self.scanButton, 2, 1, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setMinimumSize(QtCore.QSize(150, 70))
        self.saveButton.setStyleSheet("QPushButton{\n"
"image: url(:/images/images/save.png);\n"
"}")
        self.saveButton.setText("")
        self.saveButton.setObjectName("saveButton")
        self.buttons.addWidget(self.saveButton, 2, 0, 1, 1)
        self.verticalLayoutMain.addLayout(self.buttons)
        self.verticalLayout.addLayout(self.verticalLayoutMain)
        self.horizontalLayoutWorkStatus = QtWidgets.QHBoxLayout()
        self.horizontalLayoutWorkStatus.setObjectName("horizontalLayoutWorkStatus")
        self.labelWorkStatus = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelWorkStatus.setFont(font)
        self.labelWorkStatus.setObjectName("labelWorkStatus")
        self.horizontalLayoutWorkStatus.addWidget(self.labelWorkStatus)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayoutWorkStatus.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutWorkStatus.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayoutWorkStatus)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        Weights.setCentralWidget(self.centralwidget)

        self.retranslateUi(Weights)
        QtCore.QMetaObject.connectSlotsByName(Weights)
        Weights.setTabOrder(self.settingsButton, self.selectionWindow)
        Weights.setTabOrder(self.selectionWindow, self.connectButton)
        Weights.setTabOrder(self.connectButton, self.weighButton)
        Weights.setTabOrder(self.weighButton, self.calibButton)
        Weights.setTabOrder(self.calibButton, self.saveButton)
        Weights.setTabOrder(self.saveButton, self.scanButton)

    def retranslateUi(self, Weights):
        _translate = QtCore.QCoreApplication.translate
        Weights.setWindowTitle(_translate("Weights", "MainWindow"))
        self.settingsButton.setToolTip(_translate("Weights", "Дополнительно"))
        self.labelPort.setText(_translate("Weights", "Порт"))
        self.connectButton.setToolTip(_translate("Weights", "Обновить список портов"))
        self.disconnectButton.setToolTip(_translate("Weights", "Отключиться от порта"))
        self.cleanButton.setText(_translate("Weights", "Очистить"))
        self.weighButton.setToolTip(_translate("Weights", "Взвешивание"))
        self.calibButton.setToolTip(_translate("Weights", "Калибровка"))
        self.scanButton.setToolTip(_translate("Weights", "Сканирование"))
        self.saveButton.setToolTip(_translate("Weights", "Сохранение"))
        self.labelWorkStatus.setText(_translate("Weights", "Статус работы: "))
        self.label.setText(_translate("Weights", "работает"))
import icons