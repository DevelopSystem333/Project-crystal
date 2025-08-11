# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designboRWyi.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)
import icons

count = 0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(790, 637)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/white/icons/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(12, 18, 31);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(100, -30, 811, 681))
        self.tabWidget.setStyleSheet(u"background-color: transparent;\n"
"border: 0px;")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"")
        self.widget_5 = QWidget(self.tab)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(12, 114, 671, 421))
        self.widget_5.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.widget_5.setStyleSheet(u"background-color: rgb(12, 26, 57); color: white; border-radius: 5px;")
        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(10, 20, 321, 181))
        self.widget_7.setStyleSheet(u"background-color: rgb(12, 26, 100); color: white; border-radius: 5px;")
        self.textEdit_2 = QTextEdit(self.widget_7)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(0, 0, 321, 181))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setReadOnly(True)
        self.widget_11 = QWidget(self.widget_5)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(340, 20, 321, 181))
        self.widget_11.setStyleSheet(u"background-color: rgb(12, 26, 100); color: white; border-radius: 5px;")
        self.textEdit_3 = QTextEdit(self.widget_11)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(0, 0, 321, 181))
        self.textEdit_3.setFont(font)
        self.textEdit_3.setReadOnly(True)
        self.widget_12 = QWidget(self.widget_5)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setGeometry(QRect(10, 220, 321, 181))
        self.widget_12.setStyleSheet(u"background-color: rgb(12, 26, 100); color: white; border-radius: 5px;")
        self.textEdit_5 = QTextEdit(self.widget_12)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(0, 0, 321, 181))
        self.textEdit_5.setFont(font)
        self.textEdit_5.setReadOnly(True)
        self.widget_13 = QWidget(self.widget_5)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setGeometry(QRect(340, 220, 321, 181))
        self.widget_13.setStyleSheet(u"background-color: rgb(12, 26, 100); color: white; border-radius: 5px;")
        self.textEdit_4 = QTextEdit(self.widget_13)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(0, 0, 321, 181))
        self.textEdit_4.setFont(font)
        self.textEdit_4.setReadOnly(True)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.widget_4 = QWidget(self.tab_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(10, 117, 671, 421))
        self.widget_4.setStyleSheet(u"background-color: rgb(12, 26, 57); color: white; border-radius: 5px;")
        self.verticalLayoutWidget_2 = QWidget(self.widget_4)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 671, 421))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox_5 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_5.setObjectName(u"checkBox_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy1)
        self.checkBox_5.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.checkBox_5.setFont(font1)
        self.checkBox_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_5.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"	image: url(:/white/icons/icons8-\u043f\u0443\u0441\u0442\u043e\u0439-\u0447\u0435\u043a\u0431\u043e\u043a\u0441-24.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/white/icons/icons8-\u043e\u0442\u043c\u0435\u0447\u0435\u043d\u043d\u044b\u0439-\u0447\u0435\u043a\u0431\u043e\u043a\u0441-24.png);\n"
"}\n"
"QCheckBox {\n"
"	color: white;\n"
"	background-color: transparent\n"
"}")

        self.verticalLayout_2.addWidget(self.checkBox_5)

        self.checkBox_2 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy1.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy1)
        self.checkBox_2.setFont(font1)
        self.checkBox_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_2.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"	image: url(:/white/icons/icons8-\u043f\u0443\u0441\u0442\u043e\u0439-\u0447\u0435\u043a\u0431\u043e\u043a\u0441-24.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/white/icons/icons8-\u043e\u0442\u043c\u0435\u0447\u0435\u043d\u043d\u044b\u0439-\u0447\u0435\u043a\u0431\u043e\u043a\u0441-24.png);\n"
"}\n"
"QCheckBox {\n"
"	color: white;\n"
"	background-color: transparent\n"
"}")

        self.verticalLayout_2.addWidget(self.checkBox_2)

        self.checkBox_4 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_4.setObjectName(u"checkBox_4")
        sizePolicy1.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy1)
        self.checkBox_4.setFont(font1)
        self.checkBox_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_4.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"	image: url(:/white/icons/icons8-\u043f\u0443\u0441\u0442\u043e\u0439-\u0447\u0435\u043a\u0431\u043e\u043a\u0441-24.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/white/icons/icons8-\u043e\u0442\u043c\u0435\u0447\u0435\u043d\u043d\u044b\u0439-\u0447\u0435\u043a\u0431\u043e\u043a\u0441-24.png);\n"
"}\n"
"QCheckBox {\n"
"	color: white;\n"
"	background-color: transparent\n"
"}")

        self.verticalLayout_2.addWidget(self.checkBox_4)

        self.checkBox_3 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_3.setObjectName(u"checkBox_3")
        sizePolicy1.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy1)
        self.checkBox_3.setFont(font1)
        self.checkBox_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_3.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"	image: url(:/white/icons/icons8-\u043f\u0443\u0441\u0442\u043e\u0439-\u0447\u0435\u043a\u0431\u043e\u043a\u0441-24.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/white/icons/icons8-\u043e\u0442\u043c\u0435\u0447\u0435\u043d\u043d\u044b\u0439-\u0447\u0435\u043a\u0431\u043e\u043a\u0441-24.png);\n"
"}\n"
"QCheckBox {\n"
"	color: white;\n"
"	background-color: transparent\n"
"}")

        self.verticalLayout_2.addWidget(self.checkBox_3)

        self.checkBox = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy1.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy1)
        self.checkBox.setFont(font1)
        self.checkBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"	image: url(:/white/icons/icons8-\u043f\u0443\u0441\u0442\u043e\u0439-\u0447\u0435\u043a\u0431\u043e\u043a\u0441-24.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/white/icons/icons8-\u043e\u0442\u043c\u0435\u0447\u0435\u043d\u043d\u044b\u0439-\u0447\u0435\u043a\u0431\u043e\u043a\u0441-24.png);\n"
"}\n"
"QCheckBox {\n"
"	color: white;\n"
"	background-color: transparent\n"
"}")

        self.verticalLayout_2.addWidget(self.checkBox)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.widget_3 = QWidget(self.tab_4)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 117, 671, 421))
        self.widget_3.setStyleSheet(u"background-color: rgb(12, 26, 57); color: white; border-radius: 5px;")
        self.verticalLayoutWidget_5 = QWidget(self.widget_3)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(0, 0, 671, 421))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.checkBox_12 = QCheckBox(self.verticalLayoutWidget_5)
        self.checkBox_12.setObjectName(u"checkBox_12")
        sizePolicy1.setHeightForWidth(self.checkBox_12.sizePolicy().hasHeightForWidth())
        self.checkBox_12.setSizePolicy(sizePolicy1)
        self.checkBox_12.setMaximumSize(QSize(16777215, 16777215))
        self.checkBox_12.setFont(font1)
        self.checkBox_12.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_12.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"	image: url(:/white/icons/icons8-\u043f\u0443\u0441\u0442\u043e\u0439-\u0447\u0435\u043a\u0431\u043e\u043a\u0441-24.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/white/icons/icons8-\u043e\u0442\u043c\u0435\u0447\u0435\u043d\u043d\u044b\u0439-\u0447\u0435\u043a\u0431\u043e\u043a\u0441-24.png);\n"
"}\n"
"QCheckBox {\n"
"	color: white;\n"
"	background-color: transparent\n"
"}")

        self.verticalLayout_5.addWidget(self.checkBox_12)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.widget_2 = QWidget(self.tab_3)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 117, 671, 421))
        self.widget_2.setStyleSheet(u"background-color: rgb(12, 26, 57); color: white; border-radius: 5px;")
        self.verticalLayoutWidget_3 = QWidget(self.widget_2)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 671, 421))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.checkBox_6 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_6.setObjectName(u"checkBox_6")
        sizePolicy1.setHeightForWidth(self.checkBox_6.sizePolicy().hasHeightForWidth())
        self.checkBox_6.setSizePolicy(sizePolicy1)
        self.checkBox_6.setMaximumSize(QSize(16777215, 16777215))
        self.checkBox_6.setFont(font1)
        self.checkBox_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_6.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"	image: url(:/white/icons/icons8-\u043f\u0443\u0441\u0442\u043e\u0439-\u0447\u0435\u043a\u0431\u043e\u043a\u0441-24.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/white/icons/icons8-\u043e\u0442\u043c\u0435\u0447\u0435\u043d\u043d\u044b\u0439-\u0447\u0435\u043a\u0431\u043e\u043a\u0441-24.png);\n"
"}\n"
"QCheckBox {\n"
"	color: white;\n"
"	background-color: transparent\n"
"}")

        self.verticalLayout_3.addWidget(self.checkBox_6)

        self.checkBox_7 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_7.setObjectName(u"checkBox_7")
        sizePolicy1.setHeightForWidth(self.checkBox_7.sizePolicy().hasHeightForWidth())
        self.checkBox_7.setSizePolicy(sizePolicy1)
        self.checkBox_7.setFont(font1)
        self.checkBox_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_7.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"	image: url(:/white/icons/icons8-\u043f\u0443\u0441\u0442\u043e\u0439-\u0447\u0435\u043a\u0431\u043e\u043a\u0441-24.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/white/icons/icons8-\u043e\u0442\u043c\u0435\u0447\u0435\u043d\u043d\u044b\u0439-\u0447\u0435\u043a\u0431\u043e\u043a\u0441-24.png);\n"
"}\n"
"QCheckBox {\n"
"	color: white;\n"
"	background-color: transparent\n"
"}")

        self.verticalLayout_3.addWidget(self.checkBox_7)

        self.checkBox_8 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_8.setObjectName(u"checkBox_8")
        sizePolicy1.setHeightForWidth(self.checkBox_8.sizePolicy().hasHeightForWidth())
        self.checkBox_8.setSizePolicy(sizePolicy1)
        self.checkBox_8.setFont(font1)
        self.checkBox_8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_8.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"	image: url(:/white/icons/icons8-\u043f\u0443\u0441\u0442\u043e\u0439-\u0447\u0435\u043a\u0431\u043e\u043a\u0441-24.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/white/icons/icons8-\u043e\u0442\u043c\u0435\u0447\u0435\u043d\u043d\u044b\u0439-\u0447\u0435\u043a\u0431\u043e\u043a\u0441-24.png);\n"
"}\n"
"QCheckBox {\n"
"	color: white;\n"
"	background-color: transparent\n"
"}")

        self.verticalLayout_3.addWidget(self.checkBox_8)

        self.checkBox_9 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_9.setObjectName(u"checkBox_9")
        sizePolicy1.setHeightForWidth(self.checkBox_9.sizePolicy().hasHeightForWidth())
        self.checkBox_9.setSizePolicy(sizePolicy1)
        self.checkBox_9.setFont(font1)
        self.checkBox_9.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_9.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"	image: url(:/white/icons/icons8-\u043f\u0443\u0441\u0442\u043e\u0439-\u0447\u0435\u043a\u0431\u043e\u043a\u0441-24.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/white/icons/icons8-\u043e\u0442\u043c\u0435\u0447\u0435\u043d\u043d\u044b\u0439-\u0447\u0435\u043a\u0431\u043e\u043a\u0441-24.png);\n"
"}\n"
"QCheckBox {\n"
"	color: white;\n"
"	background-color: transparent\n"
"}")

        self.verticalLayout_3.addWidget(self.checkBox_9)

        self.checkBox_10 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_10.setObjectName(u"checkBox_10")
        sizePolicy1.setHeightForWidth(self.checkBox_10.sizePolicy().hasHeightForWidth())
        self.checkBox_10.setSizePolicy(sizePolicy1)
        self.checkBox_10.setFont(font1)
        self.checkBox_10.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_10.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"	image: url(:/white/icons/icons8-\u043f\u0443\u0441\u0442\u043e\u0439-\u0447\u0435\u043a\u0431\u043e\u043a\u0441-24.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/white/icons/icons8-\u043e\u0442\u043c\u0435\u0447\u0435\u043d\u043d\u044b\u0439-\u0447\u0435\u043a\u0431\u043e\u043a\u0441-24.png);\n"
"}\n"
"QCheckBox {\n"
"	color: white;\n"
"	background-color: transparent\n"
"}")

        self.verticalLayout_3.addWidget(self.checkBox_10)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.widget_8 = QWidget(self.tab_5)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(10, 117, 671, 421))
        self.widget_8.setStyleSheet(u"background-color: rgb(12, 26, 57); color: white; border-radius: 5px;")
        self.lightTheme = QPushButton(self.widget_8)
        self.lightTheme.setObjectName(u"lightTheme")
        self.lightTheme.setGeometry(QRect(14, 12, 161, 61))
        self.lightTheme.setFont(font)
        self.lightTheme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lightTheme.setStyleSheet(u"background-color: rgb(12, 26, 100); color: white; border-radius: 5px;")
        self.darkTheme = QPushButton(self.widget_8)
        self.darkTheme.setObjectName(u"darkTheme")
        self.darkTheme.setGeometry(QRect(180, 12, 161, 61))
        self.darkTheme.setFont(font)
        self.darkTheme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.darkTheme.setStyleSheet(u"background-color: rgb(12, 26, 100); color: white; border-radius: 5px;")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.widget_9 = QWidget(self.tab_6)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(10, 117, 671, 421))
        self.widget_9.setStyleSheet(u"background-color: rgb(12, 26, 57); color: white; border-radius: 5px;")
        self.textEdit = QTextEdit(self.widget_9)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 0, 671, 421))
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.widget_10 = QWidget(self.tab_7)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(10, 117, 671, 421))
        self.widget_10.setStyleSheet(u"background-color: rgb(12, 26, 57); color: white; border-radius: 5px;")
        self.horizontalLayoutWidget = QWidget(self.widget_10)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(-1, -1, 671, 351))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 0, 9, 0)
        self.addFirefox = QPushButton(self.horizontalLayoutWidget)
        self.addFirefox.setObjectName(u"addFirefox")
        self.addFirefox.setMinimumSize(QSize(55, 33))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        self.addFirefox.setFont(font2)
        self.addFirefox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addFirefox.setStyleSheet(u"background-color: rgb(12, 26, 100); color: white; border-radius: 5px;")

        self.horizontalLayout.addWidget(self.addFirefox)

        self.addVSCode = QPushButton(self.horizontalLayoutWidget)
        self.addVSCode.setObjectName(u"addVSCode")
        self.addVSCode.setMinimumSize(QSize(55, 33))
        self.addVSCode.setFont(font2)
        self.addVSCode.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addVSCode.setStyleSheet(u"background-color: rgb(12, 26, 100); color: white; border-radius: 5px;")

        self.horizontalLayout.addWidget(self.addVSCode)

        self.add7zip = QPushButton(self.horizontalLayoutWidget)
        self.add7zip.setObjectName(u"add7zip")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.add7zip.sizePolicy().hasHeightForWidth())
        self.add7zip.setSizePolicy(sizePolicy2)
        self.add7zip.setMinimumSize(QSize(55, 33))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(9)
        self.add7zip.setFont(font3)
        self.add7zip.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add7zip.setStyleSheet(u"background-color: rgb(12, 26, 100); color: white; border-radius: 5px;")

        self.horizontalLayout.addWidget(self.add7zip)

        self.pushButton_8 = QPushButton(self.widget_10)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(170, 360, 321, 51))
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"background-color: rgb(12, 26, 100); color: white; border-radius: 5px;")
        self.tabWidget.addTab(self.tab_7, "")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(7, 110, 91, 421))
        self.widget.setStyleSheet(u"background-color: rgb(12, 26, 57); color: white; border-radius: 5px;")
        self.verticalLayoutWidget = QWidget(self.widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 91, 421))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabButton4 = QPushButton(self.verticalLayoutWidget)
        self.tabButton4.setObjectName(u"tabButton4")
        self.tabButton4.setMinimumSize(QSize(0, 77))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.tabButton4.setFont(font4)
        self.tabButton4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tabButton4.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon1 = QIcon()
        icon1.addFile(u":/white/icons/icons8-\u0433\u043b\u0430\u0432\u043d\u0430\u044f-32.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabButton4.setIcon(icon1)
        self.tabButton4.setIconSize(QSize(33, 33))

        self.verticalLayout.addWidget(self.tabButton4)

        self.tabButton3 = QPushButton(self.verticalLayoutWidget)
        self.tabButton3.setObjectName(u"tabButton3")
        self.tabButton3.setMinimumSize(QSize(0, 77))
        self.tabButton3.setFont(font1)
        self.tabButton3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tabButton3.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon2 = QIcon()
        icon2.addFile(u":/white/icons/icons8-\u043c\u0443\u0441\u043e\u0440-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabButton3.setIcon(icon2)
        self.tabButton3.setIconSize(QSize(33, 33))

        self.verticalLayout.addWidget(self.tabButton3)

        self.tabButton2 = QPushButton(self.verticalLayoutWidget)
        self.tabButton2.setObjectName(u"tabButton2")
        self.tabButton2.setMinimumSize(QSize(0, 77))
        self.tabButton2.setFont(font1)
        self.tabButton2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tabButton2.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon3 = QIcon()
        icon3.addFile(u":/white/icons/icons8-\u043f\u0440\u0438\u0431\u043e\u0440\u043d\u0430\u044f-\u043f\u0430\u043d\u0435\u043b\u044c-50.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabButton2.setIcon(icon3)
        self.tabButton2.setIconSize(QSize(33, 33))

        self.verticalLayout.addWidget(self.tabButton2)

        self.tabButton5 = QPushButton(self.verticalLayoutWidget)
        self.tabButton5.setObjectName(u"tabButton5")
        self.tabButton5.setMinimumSize(QSize(0, 77))
        self.tabButton5.setFont(font1)
        self.tabButton5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tabButton5.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon4 = QIcon()
        icon4.addFile(u":/white/icons/icons8-external-setting-tweak-web-design-and-development-outline-design-circle-32.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabButton5.setIcon(icon4)
        self.tabButton5.setIconSize(QSize(33, 33))

        self.verticalLayout.addWidget(self.tabButton5)

        self.tabButton1 = QPushButton(self.verticalLayoutWidget)
        self.tabButton1.setObjectName(u"tabButton1")
        self.tabButton1.setMinimumSize(QSize(0, 77))
        self.tabButton1.setFont(font1)
        self.tabButton1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tabButton1.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon5 = QIcon()
        icon5.addFile(u":/white/icons/icons8-palette-64.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabButton1.setIcon(icon5)
        self.tabButton1.setIconSize(QSize(33, 33))

        self.verticalLayout.addWidget(self.tabButton1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(7, 540, 91, 91))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(12)
        font5.setBold(False)
        self.pushButton.setFont(font5)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(12, 26, 57); color: white; border-radius: 5px;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(15, 545, 21, 21))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: white;\n"
"background-color: transparent;")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(112, 540, 91, 91))
        self.pushButton_3.setFont(font5)
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(12, 26, 57); color: white; border-radius: 5px;")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(210, 540, 571, 91))
        self.pushButton_4.setFont(font5)
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(12, 26, 57); color: white; border-radius: 5px;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(12, 30, 81, 39))
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(18)
        font6.setBold(True)
        self.label_3.setFont(font6)
        self.label_3.setStyleSheet(u"color: white;\n"
"background-color: transparent;")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 100, 791, 2))
        self.line.setStyleSheet(u"background-color: grey;")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 535, 791, 2))
        self.line_2.setStyleSheet(u"background-color: grey;")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(104, 0, 2, 637))
        self.line_3.setStyleSheet(u"background-color: grey;")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.widget_6 = QWidget(self.centralwidget)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(112, 10, 671, 80))
        self.widget_6.setStyleSheet(u"background-color: rgb(12, 26, 57); color: white; border-radius: 5px;")
        self.pushButton_2 = QPushButton(self.widget_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(240, 0, 81, 80))
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"background-color: transparent;")
        icon6 = QIcon()
        icon6.addFile(u":/white/icons/icons8-\u0442\u0435\u043b\u0435\u0433\u0440\u0430\u043c-64.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon6)
        self.pushButton_2.setIconSize(QSize(64, 64))
        self.pushButton_5 = QPushButton(self.widget_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(330, 0, 81, 80))
        self.pushButton_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"background-color: transparent;")
        icon7 = QIcon()
        icon7.addFile(u":/white/icons/icons8-\u0442\u0438\u043a\u0442\u043e\u043a-64.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon7)
        self.pushButton_5.setIconSize(QSize(64, 64))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "")
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043f\u0430\u043f\u043a\u0443 %temp%", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043a\u044d\u0448 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0439 Windows", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043f\u0430\u043f\u043a\u0443 prefetch", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043a\u044d\u0448 \u0431\u0440\u0430\u0443\u0437\u0435\u0440\u0430", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043f\u0430\u043f\u043a\u0443 temp", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "")
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0441\u0442\u0430\u0440\u043e\u0435 \u043a\u043e\u043d\u0442\u0435\u043a\u0441\u0442\u043d\u043e\u0435 \u043c\u0435\u043d\u044e(\u0438\u0437 Windows 10)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), "")
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c Xbox Game Bar", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f Windows", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043a\u043e\u0440\u0442\u0430\u043d\u0443", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c Microsoft Edge", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c \u043d\u0430\u0438\u043b\u0443\u0447\u0448\u0435\u0435 \u0431\u044b\u0441\u0442\u0440\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435(\u0441 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435\u043c \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0430 \u0448\u0440\u0438\u0444\u0442\u043e\u0432)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), "")
        self.lightTheme.setText(QCoreApplication.translate("MainWindow", u"Light theme", None))
        self.darkTheme.setText(QCoreApplication.translate("MainWindow", u"Dark theme", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), "")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
        self.addFirefox.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c Firefox", None))
        self.addVSCode.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c VSCode", None))
        self.add7zip.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c 7zip", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
        self.tabButton4.setText("")
        self.tabButton3.setText("")
        self.tabButton2.setText("")
        self.tabButton5.setText("")
        self.tabButton1.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", f"{count}", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0439", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Crystal", None))
        self.pushButton_2.setText("")
        self.pushButton_5.setText("")
    # retranslateUi

