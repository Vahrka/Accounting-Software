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
from PySide6.QtWidgets import (QApplication, QLabel, QScrollArea, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setStyleSheet(u"/* ====================== */\n"
"/* CORE APPLICATION STYLES */\n"
"/* ====================== */\n"
"\n"
"QMainWindow {\n"
"    background-color: #f8fafc;\n"
"    font-size: 13px;\n"
"    color: #374151;\n"
"}\n"
"\n"
"/* ====================== */\n"
"/* ENHANCED NAVBAR STYLES */\n"
"/* ====================== */\n"
"\n"
"/* This is the Menu \"BAR\" it self */\n"
"QMenuBar {\n"
"    background-color: #ffffff;\n"
"    padding: 8px 0;\n"
"    margin: 0;\n"
"    outline: 0;\n"
"    border-bottom: 1px solid #e5e7eb;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"/* This is the Top Menubar each item but not its content */\n"
"QMenuBar::item {\n"
"    padding: 8px 14px;\n"
"    margin: 0 6px;\n"
"    border-radius: 6px;\n"
"    color: #4b5563;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:hover {\n"
"    background-color: #f3f4f6;\n"
"    color: #1d4ed8;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background-color: #eff6ff;\n"
"    color: #1d4ed8;\n"
"    font-weight: 600"
                        ";\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"    background-color: #e5e7eb;\n"
"}\n"
"\n"
"QMenuBar::icon {\n"
"    margin-right: 12px;\n"
"    left: 12px;\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"\n"
"/* ====================== */\n"
"/* SIDE NAVIGATION STYLES */\n"
"/* ====================== */\n"
"\n"
"#MainSideNavFrame {\n"
"    background-color: #fafcfe;\n"
"    border: 3px solid #e5e7eb;\n"
"    padding: 8px 0;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#MainSideNavFrame QPushButton { /* The btns inside navbar */\n"
"    min-width: 50px;\n"
"    max-width: 200px;\n"
"    padding: 10px 35px 10px 10px;\n"
"    border-left: 5px solid #6453fe;\n"
"    margin: 0px 8px;\n"
"    border-top-left-radius: 0;\n"
"    border-bottom-left-radius: 0;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    font-size: 14px;\n"
"    font-weight: 400;\n"
"    color: #4b5563;\n"
"    text-align: left;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#MainSideNavFrame QPushBut"
                        "ton:hover {\n"
"    background-color: #f3f4f6;\n"
"    color: #1d4ed8;\n"
"    border-left: 5px solid #ff006a;\n"
"}\n"
"\n"
"\n"
"#MainSideNavFrame QPushButton::icon {\n"
"    margin-right: 12px;\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"\n"
"/* ====================== */\n"
"/* BUTTON STYLES */\n"
"/* ====================== */\n"
"\n"
"QPushButton {\n"
"    min-width: 90px;\n"
"    padding: 8px 16px;\n"
"    border-radius: 6px;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"    border: 1px solid #d1d5db;\n"
"    background-color: #ffffff;\n"
"    color: #374151;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f9fafb;\n"
"    border-color: #9ca3af;\n"
"    color: #1d4ed8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f3f4f6;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #9ca3af;\n"
"    background-color: #f8f9fa;\n"
"}\n"
"\n"
"QPushButton.primary {\n"
"    background-color: #2563eb;\n"
"    border-color: #2563eb;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
""
                        "QPushButton.primary:hover {\n"
"    background-color: #1d4ed8;\n"
"    border-color: #1d4ed8;\n"
"}\n"
"\n"
"QPushButton.danger {\n"
"    background-color: #dc2626;\n"
"    border-color: #dc2626;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton.danger:hover {\n"
"    background-color: #b91c1c;\n"
"    border-color: #b91c1c;\n"
"}\n"
"\n"
"/* ====================== */\n"
"/* PLUGIN MANAGER STYLES */\n"
"/* ====================== */\n"
"\n"
"QDialog#pluginManager {\n"
"    background-color: #ffffff;\n"
"    border-radius: 15px;\n"
"    padding: 12px;\n"
"    border: 1px solid #e5e7eb;\n"
"}\n"
"\n"
"QDialog #pluginList {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QDialog #pluginList:item::hover {\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QDialog #pluginList:item::selected {\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"}"
                        "\n"
"\n"
"QDialog #pluginList:item::focus {\n"
"    border: 1px solid #e2e8f0;\n"
"    background: #fff;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"#pluginCheckbox {\n"
"    spacing: 10px;\n"
"    font-size: 13px;\n"
"    padding: 4px 0;\n"
"    color: #374151;\n"
"}\n"
"\n"
"#pluginCheckbox::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 6px;\n"
"    border: 1px solid #cbd5e1;\n"
"}\n"
"\n"
"#pluginCheckbox::indicator:checked {\n"
"    background-color: #3b82f6;\n"
"    border-color: #2563eb;\n"
"    border: 2px solid #cbd5e1;\n"
"}\n"
"\n"
"#pluginDeleteBtn {\n"
"    min-width: 80px;\n"
"    padding: 7px 14px;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"    border-radius: 6px;\n"
"    background-color: #fef2f2;\n"
"    border: 1px solid #fee2e2;\n"
"    color: #b91c1c;\n"
"}\n"
"\n"
"#pluginDeleteBtn:hover {\n"
"    background-color: #fee2e2;\n"
"    border-color: #fecaca;\n"
"    border: 1px solid #cbd5e1;\n"
"}\n"
"\n"
"/* ==============="
                        "======= */\n"
"/* MENU STYLES */\n"
"/* ====================== */\n"
"\n"
"QMenu.menubar-menu {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e5e7eb;\n"
"    border-radius: 8px;\n"
"    font-size: 13px;\n"
"    color: #374151;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QMenu.menubar-menu::item {\n"
"    padding: 8px 14px;\n"
"    /* padding: 8px 24px 8px 36px; */\n"
"    border-radius: 0;\n"
"}\n"
"\n"
"QMenu.menubar-menu::item:selected {\n"
"    background-color: #f3f4f6;\n"
"    color: #1d4ed8;\n"
"}\n"
"\n"
"QMenu.menubar-menu::item:selected:first {\n"
"    border-top-right-radius: 8px;\n"
"}\n"
"\n"
"QMenu.menubar-menu::item:selected:last {\n"
"    border-bottom-right-radius: 8px;\n"
"}\n"
"\n"
"QMenu.menubar-menu::icon {\n"
"    margin: 0 12px 0 6px;\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"\n"
"/* ====================== */\n"
"/* SCROLLBAR STYLES */\n"
"/* ====================== */\n"
"\n"
"/* ===== MODERN SCROLLBARS WITH NO CORNER ARTIFACTS ===== */\n"
"/* Applies to all QScrol"
                        "lBars in the application */\n"
"\n"
"/* --- COMPLETELY REMOVE RESIZE CORNER --- */\n"
"QScrollBar::corner,\n"
"QAbstractScrollArea::corner {\n"
"    background: transparent;\n"
"    border: none;\n"
"    width: 0;\n"
"    height: 0;\n"
"}\n"
"\n"
"/* --- VERTICAL SCROLLBAR --- */\n"
"QScrollBar:vertical {\n"
"    width: 12px;\n"
"    background: #f1f5f9;\n"
"    border-radius: 6px;\n"
"    margin: 0;\n"
"    padding: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #cbd5e1;\n"
"    min-height: 30px;\n"
"    border-radius: 6px;\n"
"    margin: 12px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #9ca3af;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 12px;\n"
"    background: #e2e8f0;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover,\n"
"QScrollBar::sub-line:vertical:hover {\n"
"    background: #cbd5e1;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed,\n"
"QScrollBar::sub-line:vertic"
                        "al:pressed {\n"
"    background: #9ca3af;\n"
"}\n"
"\n"
"/* --- HORIZONTAL SCROLLBAR --- */\n"
"QScrollBar:horizontal {\n"
"    height: 12px;\n"
"    background: #f1f5f9;\n"
"    border-radius: 6px;\n"
"    margin: 0;\n"
"    padding: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #cbd5e1;\n"
"    min-width: 30px;\n"
"    border-radius: 6px;\n"
"    margin: 0 12px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #9ca3af;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    width: 12px;\n"
"    background: #e2e8f0;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"    background: #cbd5e1;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed,\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"    background: #9ca3af;\n"
"}\n"
"\n"
"\n"
"/* ====================== */\n"
"/* TEXT INPUT STYLES */\n"
"/* ====================== */\n"
"\n"
"QLineEdit, "
                        "QTextEdit {\n"
"    border: 1px solid #d1d5db;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    font-size: 13px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus {\n"
"    border-color: #3b82f6;\n"
"}\n"
"\n"
"/* ===== Modern Borderless QTabWidget ===== */\n"
"\n"
"* {\n"
"    border: none;\n"
"}\n"
"\n"
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
"    min-wi"
                        "dth: 80px;\n"
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
        self.Invoices = QWidget()
        self.Invoices.setObjectName(u"Invoices")
        self.vboxLayout = QVBoxLayout(self.Invoices)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.scrollArea = QScrollArea(self.Invoices)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollarea_qwidget = QWidget()
        self.scrollarea_qwidget.setObjectName(u"scrollarea_qwidget")
        self.scrollarea_qwidget_layout = QVBoxLayout(self.scrollarea_qwidget)
        self.scrollarea_qwidget_layout.setObjectName(u"scrollarea_qwidget_layout")
        self.scrollarea_qwidget_layout.setContentsMargins(0, 0, 0, -1)
        self.frame = QWidget(self.scrollarea_qwidget)
        self.frame.setObjectName(u"frame")
        self.frame_verticalLayout = QVBoxLayout(self.frame)
        self.frame_verticalLayout.setObjectName(u"frame_verticalLayout")
        self.frame_invoice = QWidget(self.frame)
        self.frame_invoice.setObjectName(u"frame_invoice")
        self.frame_invoice_layout = QVBoxLayout(self.frame_invoice)
        self.frame_invoice_layout.setObjectName(u"frame_invoice_layout")
        self.label_new_invoice = QLabel(self.frame_invoice)
        self.label_new_invoice.setObjectName(u"label_new_invoice")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_new_invoice.setFont(font)
        self.label_new_invoice.setWordWrap(True)

        self.frame_invoice_layout.addWidget(self.label_new_invoice)

        self.label_company = QLabel(self.frame_invoice)
        self.label_company.setObjectName(u"label_company")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setWeight(QFont.DemiBold)
        self.label_company.setFont(font1)
        self.label_company.setWordWrap(True)

        self.frame_invoice_layout.addWidget(self.label_company)

        self.label_subtitle = QLabel(self.frame_invoice)
        self.label_subtitle.setObjectName(u"label_subtitle")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_subtitle.sizePolicy().hasHeightForWidth())
        self.label_subtitle.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(12)
        self.label_subtitle.setFont(font2)
        self.label_subtitle.setStyleSheet(u"color: rgb(154, 153, 150)")
        self.label_subtitle.setWordWrap(True)

        self.frame_invoice_layout.addWidget(self.label_subtitle)


        self.frame_verticalLayout.addWidget(self.frame_invoice, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_billing = QWidget(self.frame)
        self.frame_billing.setObjectName(u"frame_billing")
        self.frame_billing_layout = QVBoxLayout(self.frame_billing)
        self.frame_billing_layout.setObjectName(u"frame_billing_layout")
        self.label_billing = QLabel(self.frame_billing)
        self.label_billing.setObjectName(u"label_billing")
        self.label_billing.setFont(font)
        self.label_billing.setWordWrap(True)

        self.frame_billing_layout.addWidget(self.label_billing)


        self.frame_verticalLayout.addWidget(self.frame_billing, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_advanced = QWidget(self.frame)
        self.frame_advanced.setObjectName(u"frame_advanced")
        self.frame_advanced_layout = QVBoxLayout(self.frame_advanced)
        self.frame_advanced_layout.setObjectName(u"frame_advanced_layout")
        self.label_advanced = QLabel(self.frame_advanced)
        self.label_advanced.setObjectName(u"label_advanced")
        self.label_advanced.setFont(font)
        self.label_advanced.setWordWrap(True)

        self.frame_advanced_layout.addWidget(self.label_advanced)


        self.frame_verticalLayout.addWidget(self.frame_advanced, 0, Qt.AlignmentFlag.AlignTop)


        self.scrollarea_qwidget_layout.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignTop)

        self.scrollArea.setWidget(self.scrollarea_qwidget)

        self.vboxLayout.addWidget(self.scrollArea)

        Form.addTab(self.Invoices, "")
        self.Customers = QWidget()
        self.Customers.setObjectName(u"Customers")
        Form.addTab(self.Customers, "")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.label_new_invoice.setText(QCoreApplication.translate("Form", u"New Invoice", None))
        self.label_company.setText(QCoreApplication.translate("Form", u"Company", None))
        self.label_subtitle.setText(QCoreApplication.translate("Form", u"Change the address, logo, and other information for your company.", None))
        self.label_billing.setText(QCoreApplication.translate("Form", u"Billing", None))
        self.label_advanced.setText(QCoreApplication.translate("Form", u"Advanced", None))
        Form.setTabText(Form.indexOf(self.Invoices), QCoreApplication.translate("Form", u"Page", None))
        Form.setTabText(Form.indexOf(self.Customers), QCoreApplication.translate("Form", u"Page", None))
        pass
    # retranslateUi

