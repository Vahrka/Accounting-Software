# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)
import source_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 720)
        MainWindow.setMinimumSize(QSize(1024, 720))
        self.actionContact = QAction(MainWindow)
        self.actionContact.setObjectName(u"actionContact")
        icon = QIcon()
        icon.addFile(u":/icons/contact-phonebook-support.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionContact.setIcon(icon)
        self.actionInfo = QAction(MainWindow)
        self.actionInfo.setObjectName(u"actionInfo")
        icon1 = QIcon()
        icon1.addFile(u":/icons/info-square.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionInfo.setIcon(icon1)
        self.actionRegister = QAction(MainWindow)
        self.actionRegister.setObjectName(u"actionRegister")
        icon2 = QIcon()
        icon2.addFile(u":/icons/register.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionRegister.setIcon(icon2)
        self.actionList = QAction(MainWindow)
        self.actionList.setObjectName(u"actionList")
        icon3 = QIcon()
        icon3.addFile(u":/icons/list.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionList.setIcon(icon3)
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        icon4 = QIcon()
        icon4.addFile(u":/icons/import.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionImport.setIcon(icon4)
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        icon5 = QIcon()
        icon5.addFile(u":/icons/export.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionExport.setIcon(icon5)
        self.actionPrefrences = QAction(MainWindow)
        self.actionPrefrences.setObjectName(u"actionPrefrences")
        icon6 = QIcon()
        icon6.addFile(u":/icons/preferences.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionPrefrences.setIcon(icon6)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        icon7 = QIcon()
        icon7.addFile(u":/icons/help.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionHelp.setIcon(icon7)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.MainSideNavFrame = QFrame(self.centralwidget)
        self.MainSideNavFrame.setObjectName(u"MainSideNavFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MainSideNavFrame.sizePolicy().hasHeightForWidth())
        self.MainSideNavFrame.setSizePolicy(sizePolicy1)
        self.MainSideNavFrame.setMinimumSize(QSize(100, 0))
        self.MainSideNavFrame.setMaximumSize(QSize(224, 16777215))
        self.MainSideNavFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.MainSideNavFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.MainSideNavFrame.setLineWidth(3)
        self.MainSideNavFrame.setMidLineWidth(3)
        self.verticalLayout = QVBoxLayout(self.MainSideNavFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MainSideNav = QVBoxLayout()
        self.MainSideNav.setObjectName(u"MainSideNav")
        self.MainSideNav.setContentsMargins(9, 10, 9, 10)

        self.verticalLayout.addLayout(self.MainSideNav)


        self.horizontalLayout.addWidget(self.MainSideNavFrame)

        self.MainStackView = QStackedWidget(self.centralwidget)
        self.MainStackView.setObjectName(u"MainStackView")

        self.horizontalLayout.addWidget(self.MainStackView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1024, 23))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuPlugins = QMenu(self.menuFile)
        self.menuPlugins.setObjectName(u"menuPlugins")
        icon8 = QIcon()
        icon8.addFile(u":/icons/plugin-2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuPlugins.setIcon(icon8)
        self.menuData = QMenu(self.menuFile)
        self.menuData.setObjectName(u"menuData")
        icon9 = QIcon()
        icon9.addFile(u":/icons/data.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuData.setIcon(icon9)
        self.menuSettings = QMenu(self.menuBar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.menuPlugins.menuAction())
        self.menuFile.addAction(self.menuData.menuAction())
        self.menuPlugins.addAction(self.actionRegister)
        self.menuPlugins.addAction(self.actionList)
        self.menuData.addAction(self.actionImport)
        self.menuData.addAction(self.actionExport)
        self.menuSettings.addAction(self.actionPrefrences)
        self.menuHelp.addAction(self.actionContact)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionInfo)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Accounting Software", None))
        self.actionContact.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
#if QT_CONFIG(shortcut)
        self.actionContact.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F1", None))
#endif // QT_CONFIG(shortcut)
        self.actionInfo.setText(QCoreApplication.translate("MainWindow", u"Info", None))
#if QT_CONFIG(shortcut)
        self.actionInfo.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+F1", None))
#endif // QT_CONFIG(shortcut)
        self.actionRegister.setText(QCoreApplication.translate("MainWindow", u"Register", None))
#if QT_CONFIG(shortcut)
        self.actionRegister.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionList.setText(QCoreApplication.translate("MainWindow", u"List", None))
#if QT_CONFIG(shortcut)
        self.actionList.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+X", None))
#endif // QT_CONFIG(shortcut)
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.actionPrefrences.setText(QCoreApplication.translate("MainWindow", u"Prefrences", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
#if QT_CONFIG(shortcut)
        self.actionHelp.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuFile.setProperty(u"class", QCoreApplication.translate("MainWindow", u"menubar-menu", None))
        self.menuPlugins.setTitle(QCoreApplication.translate("MainWindow", u"Plugins", None))
        self.menuPlugins.setProperty(u"class", QCoreApplication.translate("MainWindow", u"menubar-menu", None))
        self.menuData.setTitle(QCoreApplication.translate("MainWindow", u"Data", None))
        self.menuData.setProperty(u"class", QCoreApplication.translate("MainWindow", u"menubar-menu", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuSettings.setProperty(u"class", QCoreApplication.translate("MainWindow", u"menubar-menu", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuHelp.setProperty(u"class", QCoreApplication.translate("MainWindow", u"menubar-menu", None))
    # retranslateUi

