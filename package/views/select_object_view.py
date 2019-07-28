# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../resources/ui/select_object.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_selectBookTypeWindow(object):
    def setupUi(self, selectBookTypeWindow):
        selectBookTypeWindow.setObjectName("selectBookTypeWindow")
        selectBookTypeWindow.resize(300, 200)
        selectBookTypeWindow.setMinimumSize(QtCore.QSize(300, 200))
        selectBookTypeWindow.setMaximumSize(QtCore.QSize(300, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        selectBookTypeWindow.setWindowIcon(icon)
        selectBookTypeWindow.setStyleSheet("background-color: rgb(233, 185, 110);")
        self.gridLayoutWidget = QtWidgets.QWidget(selectBookTypeWindow)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 281, 185))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.selectBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.selectBtn.setFont(font)
        self.selectBtn.setStyleSheet("background-color: rgb(117, 94, 59);\n"
"color: rgb(255, 255, 255);")
        self.selectBtn.setAutoDefault(False)
        self.selectBtn.setObjectName("selectBtn")
        self.gridLayout.addWidget(self.selectBtn, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 10, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.schoolbookSelector = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.schoolbookSelector.setFont(font)
        self.schoolbookSelector.setStyleSheet("color: rgb(117, 94, 59);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icons/school.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.schoolbookSelector.setIcon(icon1)
        self.schoolbookSelector.setIconSize(QtCore.QSize(48, 48))
        self.schoolbookSelector.setObjectName("schoolbookSelector")
        self.verticalLayout.addWidget(self.schoolbookSelector)
        self.fictionbookSelector = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fictionbookSelector.setFont(font)
        self.fictionbookSelector.setStyleSheet("color: rgb(117, 94, 59);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icons/fiction.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fictionbookSelector.setIcon(icon2)
        self.fictionbookSelector.setIconSize(QtCore.QSize(48, 48))
        self.fictionbookSelector.setObjectName("fictionbookSelector")
        self.verticalLayout.addWidget(self.fictionbookSelector)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(selectBookTypeWindow)
        QtCore.QMetaObject.connectSlotsByName(selectBookTypeWindow)

    def retranslateUi(self, selectBookTypeWindow):
        _translate = QtCore.QCoreApplication.translate
        selectBookTypeWindow.setWindowTitle(_translate("selectBookTypeWindow", "Выберите тип книги"))
        self.selectBtn.setText(_translate("selectBookTypeWindow", "Выбрать"))
        self.schoolbookSelector.setText(_translate("selectBookTypeWindow", "Учебник"))
        self.fictionbookSelector.setText(_translate("selectBookTypeWindow", "Художественная книга"))

import package.views.images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    selectBookTypeWindow = QtWidgets.QDialog()
    ui = Ui_selectBookTypeWindow()
    ui.setupUi(selectBookTypeWindow)
    selectBookTypeWindow.show()
    sys.exit(app.exec_())

