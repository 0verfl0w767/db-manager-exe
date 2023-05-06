# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dbFind.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(664, 771)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.label_PK = QLabel(self.centralwidget)
        self.label_PK.setObjectName(u"label_PK")

        self.horizontalLayout_1.addWidget(self.label_PK)

        self.lineEdit_PK = QLineEdit(self.centralwidget)
        self.lineEdit_PK.setObjectName(u"lineEdit_PK")

        self.horizontalLayout_1.addWidget(self.lineEdit_PK)

        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.horizontalLayout_1.addWidget(self.pushButton_1)


        self.gridLayout.addLayout(self.horizontalLayout_1, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_SN2 = QLabel(self.centralwidget)
        self.label_SN2.setObjectName(u"label_SN2")

        self.horizontalLayout_3.addWidget(self.label_SN2)

        self.lineEdit_SN2 = QLineEdit(self.centralwidget)
        self.lineEdit_SN2.setObjectName(u"lineEdit_SN2")

        self.horizontalLayout_3.addWidget(self.lineEdit_SN2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_3.addWidget(self.pushButton_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.tableWidget, 5, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_SN1 = QLabel(self.centralwidget)
        self.label_SN1.setObjectName(u"label_SN1")

        self.horizontalLayout_2.addWidget(self.label_SN1)

        self.lineEdit_SN1 = QLineEdit(self.centralwidget)
        self.lineEdit_SN1.setObjectName(u"lineEdit_SN1")

        self.horizontalLayout_2.addWidget(self.lineEdit_SN1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")

        self.horizontalLayout_5.addWidget(self.label_1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(True)

        self.horizontalLayout_5.addWidget(self.pushButton_5)


        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_SA = QLabel(self.centralwidget)
        self.label_SA.setObjectName(u"label_SA")

        self.horizontalLayout_4.addWidget(self.label_SA)

        self.lineEdit_SA = QLineEdit(self.centralwidget)
        self.lineEdit_SA.setObjectName(u"lineEdit_SA")

        self.horizontalLayout_4.addWidget(self.lineEdit_SA)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_4.addWidget(self.pushButton_4)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 664, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"dbFind", None))
        self.label_PK.setText(QCoreApplication.translate("MainWindow", u"PK", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.label_SN2.setText(QCoreApplication.translate("MainWindow", u"Student Name", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\uace0\uc720\ubc88\ud638", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\ud559\ubc88", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\uc774\ub984", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\uae08\uc561", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\ube44\uace0", None));
        self.label_SN1.setText(QCoreApplication.translate("MainWindow", u"Student Id", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Text3", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Text4", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Text5", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"All Find", None))
        self.label_SA.setText(QCoreApplication.translate("MainWindow", u"Student Amount", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Find", None))
    # retranslateUi

