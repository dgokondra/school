# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../resources/ui/start.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1147, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(233, 185, 110);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.books_tab = QtWidgets.QTabWidget(self.central_widget)
        self.books_tab.setStyleSheet("background-color: rgb(117, 94, 59);\n"
"color: rgb(255, 255, 255);")
        self.books_tab.setObjectName("books_tab")
        self.schoolbooks_tab = QtWidgets.QWidget()
        self.schoolbooks_tab.setObjectName("schoolbooks_tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.schoolbooks_tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.schoolbooks_table_view = QtWidgets.QTableView(self.schoolbooks_tab)
        self.schoolbooks_table_view.setStyleSheet("background-color: rgb(244, 217, 173);\n"
"color: rgb(117, 94, 59);\n"
"font: 81 9pt \"Open Sans\";")
        self.schoolbooks_table_view.setObjectName("schoolbooks_table_view")
        self.horizontalLayout_3.addWidget(self.schoolbooks_table_view)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icons/schoolbookTabImage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.books_tab.addTab(self.schoolbooks_tab, icon1, "")
        self.fictionbooks_tab = QtWidgets.QWidget()
        self.fictionbooks_tab.setObjectName("fictionbooks_tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fictionbooks_tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fictionbooks_table_view = QtWidgets.QTableView(self.fictionbooks_tab)
        self.fictionbooks_table_view.setStyleSheet("background-color: rgb(244, 217, 173);")
        self.fictionbooks_table_view.setObjectName("fictionbooks_table_view")
        self.fictionbooks_table_view.verticalHeader().setSortIndicatorShown(True)
        self.horizontalLayout_2.addWidget(self.fictionbooks_table_view)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icons/fictionbookTabImage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.books_tab.addTab(self.fictionbooks_tab, icon2, "")
        self.horizontalLayout.addWidget(self.books_tab)
        MainWindow.setCentralWidget(self.central_widget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.statusbar.setFont(font)
        self.statusbar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolbar = QtWidgets.QToolBar(MainWindow)
        self.toolbar.setIconSize(QtCore.QSize(32, 32))
        self.toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolbar.setObjectName("toolbar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar)
        self.add_book_btn = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icons/addBookToolbarImage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_book_btn.setIcon(icon3)
        self.add_book_btn.setObjectName("add_book_btn")
        self.search_book_btn = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icons/searchBookToolbarImage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_book_btn.setIcon(icon4)
        self.search_book_btn.setObjectName("search_book_btn")
        self.unload_book_btn = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icons/unloadBookToolbarImage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.unload_book_btn.setIcon(icon5)
        self.unload_book_btn.setObjectName("unload_book_btn")
        self.help_btn = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/icons/helpToolbarImage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help_btn.setIcon(icon6)
        self.help_btn.setObjectName("help_btn")
        self.exit_btn = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/icons/exitToolbarImage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn.setIcon(icon7)
        self.exit_btn.setObjectName("exit_btn")
        self.toolbar.addAction(self.search_book_btn)
        self.toolbar.addAction(self.add_book_btn)
        self.toolbar.addAction(self.unload_book_btn)
        self.toolbar.addAction(self.help_btn)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.exit_btn)

        self.retranslateUi(MainWindow)
        self.books_tab.setCurrentIndex(0)
        self.exit_btn.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Школьная библиотека"))
        self.books_tab.setTabText(self.books_tab.indexOf(self.schoolbooks_tab), _translate("MainWindow", "Учебники"))
        self.books_tab.setTabText(self.books_tab.indexOf(self.fictionbooks_tab), _translate("MainWindow", "Худ.литература"))
        self.toolbar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.add_book_btn.setText(_translate("MainWindow", "Добавить"))
        self.search_book_btn.setText(_translate("MainWindow", "Найти"))
        self.unload_book_btn.setText(_translate("MainWindow", "Выгрузить"))
        self.help_btn.setText(_translate("MainWindow", "Справка"))
        self.exit_btn.setText(_translate("MainWindow", "Выход"))

import package.views.images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

