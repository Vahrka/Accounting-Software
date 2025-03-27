# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QScrollArea, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(819, 762)
        Form.setStyleSheet(u"/* ===== Modern Borderless QTabWidget ===== */\n"
"QTabWidget {\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Remove all borders from the content pane */\n"
"QTabWidget::pane {\n"
"    border: 0;\n"
"    margin: 0;\n"
"    padding: 0;\n"
"    top: -1px; /* Seamless connection with tab bar */\n"
"}\n"
"\n"
"/* Tab bar styling */\n"
"QTabBar {\n"
"    background: transparent;\n"
"    spacing: 4px;\n"
"}\n"
"\n"
"/* Individual tab styling */\n"
"QTabBar::tab {\n"
"    background: #f5f5f5;\n"
"    color: #555;\n"
"    border: 0;\n"
"    border-radius: 6px 6px 0 0;\n"
"    padding: 8px 20px;\n"
"    margin-right: 2px;\n"
"    font-family: 'Segoe UI', system-ui, sans-serif;\n"
"    font-size: 11pt;\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"/* Selected tab */\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"    color: #5900ff;\n"
"    border-bottom: 3px solid #5900ff;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QTabBar::tab:hover:!selected {\n"
"    background: #e0e0e0;\n"
"}\n"
"\n"
""
                        "/* Disabled tab */\n"
"QTabBar::tab:disabled {\n"
"    color: #aaa;\n"
"    background: #f0f0f0;\n"
"}\n"
"\n"
"/* Left/right scroll buttons (when tabs overflow) */\n"
"QTabBar QToolButton {\n"
"    background: #f0f0f0;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"QScrollArea {\n"
"    background: transparent;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabs = QTabWidget(Form)
        self.tabs.setObjectName(u"tabs")
        self.Invoices_tab = QWidget()
        self.Invoices_tab.setObjectName(u"Invoices_tab")
        self.gridLayout = QGridLayout(self.Invoices_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(self.Invoices_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(500, 700))
        self.scrollArea.setStyleSheet(u"border: none;")
        self.scrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.scrollArea.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.scrollbar = QWidget()
        self.scrollbar.setObjectName(u"scrollbar")
        self.scrollbar.setGeometry(QRect(2, 0, 797, 700))
        self.verticalLayout_2 = QVBoxLayout(self.scrollbar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(8, 8, 8, 8)
        self.company_area = QVBoxLayout()
        self.company_area.setSpacing(0)
        self.company_area.setObjectName(u"company_area")
        self.company_area.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.company_area.setContentsMargins(0, 0, 0, 0)
        self.new_invoice = QLabel(self.scrollbar)
        self.new_invoice.setObjectName(u"new_invoice")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_invoice.sizePolicy().hasHeightForWidth())
        self.new_invoice.setSizePolicy(sizePolicy)
        self.new_invoice.setMaximumSize(QSize(16777215, 25))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.new_invoice.setFont(font)

        self.company_area.addWidget(self.new_invoice)

        self.company = QLabel(self.scrollbar)
        self.company.setObjectName(u"company")
        sizePolicy.setHeightForWidth(self.company.sizePolicy().hasHeightForWidth())
        self.company.setSizePolicy(sizePolicy)
        self.company.setMaximumSize(QSize(16777215, 25))
        font1 = QFont()
        font1.setPointSize(14)
        self.company.setFont(font1)

        self.company_area.addWidget(self.company)

        self.note = QLabel(self.scrollbar)
        self.note.setObjectName(u"note")
        sizePolicy.setHeightForWidth(self.note.sizePolicy().hasHeightForWidth())
        self.note.setSizePolicy(sizePolicy)
        self.note.setMaximumSize(QSize(16777215, 25))

        self.company_area.addWidget(self.note)


        self.verticalLayout_2.addLayout(self.company_area)

        self.billing_area = QHBoxLayout()
        self.billing_area.setSpacing(0)
        self.billing_area.setObjectName(u"billing_area")
        self.label = QLabel(self.scrollbar)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.billing_area.addWidget(self.label)


        self.verticalLayout_2.addLayout(self.billing_area)

        self.advanced_area = QHBoxLayout()
        self.advanced_area.setSpacing(0)
        self.advanced_area.setObjectName(u"advanced_area")
        self.label_2 = QLabel(self.scrollbar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.advanced_area.addWidget(self.label_2)


        self.verticalLayout_2.addLayout(self.advanced_area)

        self.scrollArea.setWidget(self.scrollbar)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.tabs.addTab(self.Invoices_tab, "")
        self.Customers_tab = QWidget()
        self.Customers_tab.setObjectName(u"Customers_tab")
        self.tabs.addTab(self.Customers_tab, "")

        self.verticalLayout.addWidget(self.tabs, 0, Qt.AlignmentFlag.AlignTop)


        self.retranslateUi(Form)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.new_invoice.setText(QCoreApplication.translate("Form", u"New Invoice", None))
        self.company.setText(QCoreApplication.translate("Form", u"Company", None))
        self.note.setText(QCoreApplication.translate("Form", u"Change the address, logo, and other information for your company. ", None))
        self.label.setText(QCoreApplication.translate("Form", u"Billing", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Advanced", None))
        self.tabs.setTabText(self.tabs.indexOf(self.Invoices_tab), QCoreApplication.translate("Form", u"Tab 1", None))
        self.tabs.setTabText(self.tabs.indexOf(self.Customers_tab), QCoreApplication.translate("Form", u"Tab 2", None))
    # retranslateUi

