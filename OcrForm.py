# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\40_Programing\01_python\20210313_OCR\OcrForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets


class Ui_form_OCR(object):
    def setupUi(self, form_OCR):
        form_OCR.setObjectName("form_OCR")
        form_OCR.resize(362, 240)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(form_OCR)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_add = QtWidgets.QPushButton(form_OCR)
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout.addWidget(self.pushButton_add)
        self.pushButton_remove = QtWidgets.QPushButton(form_OCR)
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.verticalLayout.addWidget(self.pushButton_remove)
        self.pushButton_clearAll = QtWidgets.QPushButton(form_OCR)
        self.pushButton_clearAll.setObjectName("pushButton_clearAll")
        self.verticalLayout.addWidget(self.pushButton_clearAll)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_config = QtWidgets.QComboBox(form_OCR)
        self.comboBox_config.setObjectName("comboBox_config")
        self.comboBox_config.addItem("")
        self.comboBox_config.addItem("")
        self.comboBox_config.addItem("")
        self.comboBox_config.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_config)
        self.toolButton_config = QtWidgets.QToolButton(form_OCR)
        self.toolButton_config.setEnabled(True)
        self.toolButton_config.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_config.setObjectName("toolButton_config")
        self.horizontalLayout.addWidget(self.toolButton_config)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_convert = QtWidgets.QPushButton(form_OCR)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_convert.sizePolicy().hasHeightForWidth())
        self.pushButton_convert.setSizePolicy(sizePolicy)
        self.pushButton_convert.setObjectName("pushButton_convert")
        self.verticalLayout.addWidget(self.pushButton_convert)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget = QtWidgets.QListWidget(form_OCR)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(40, 40))
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.retranslateUi(form_OCR)
        self.pushButton_convert.clicked['bool'].connect(form_OCR.convert)
        self.pushButton_add.clicked.connect(form_OCR.add)
        self.pushButton_remove.clicked.connect(form_OCR.remove)
        self.pushButton_clearAll.clicked.connect(form_OCR.clearAll)
        QtCore.QMetaObject.connectSlotsByName(form_OCR)
        form_OCR.setTabOrder(self.pushButton_add, self.pushButton_remove)
        form_OCR.setTabOrder(self.pushButton_remove, self.comboBox_config)
        form_OCR.setTabOrder(self.comboBox_config, self.toolButton_config)
        form_OCR.setTabOrder(self.toolButton_config, self.pushButton_convert)
        form_OCR.setTabOrder(self.pushButton_convert, self.listWidget)

    def retranslateUi(self, form_OCR):
        _translate = QtCore.QCoreApplication.translate
        form_OCR.setWindowTitle(_translate("form_OCR", "OCR"))
        self.pushButton_add.setText(_translate("form_OCR", "Add"))
        self.pushButton_remove.setText(_translate("form_OCR", "Remove"))
        self.pushButton_clearAll.setText(_translate("form_OCR", "Clear all"))
        self.comboBox_config.setItemText(0, _translate("form_OCR", "JP vert"))
        self.comboBox_config.setItemText(1, _translate("form_OCR", "JP hor"))
        self.comboBox_config.setItemText(2, _translate("form_OCR", "ENG"))
        self.comboBox_config.setItemText(3, _translate("form_OCR", "Custom"))
        self.toolButton_config.setText(_translate("form_OCR", "..."))
        self.pushButton_convert.setText(_translate("form_OCR", "Convert!"))
