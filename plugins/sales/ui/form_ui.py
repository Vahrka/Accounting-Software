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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1470, 744)
        self.Invoices = QWidget()
        self.Invoices.setObjectName(u"Invoices")
        self.vboxLayout = QVBoxLayout(self.Invoices)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.save_btn = QPushButton(self.Invoices)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(200, 0))
        self.save_btn.setMaximumSize(QSize(350, 16777215))

        self.vboxLayout.addWidget(self.save_btn, 0, Qt.AlignmentFlag.AlignRight)

        self.scrollArea = QScrollArea(self.Invoices)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollarea_qwidget = QWidget()
        self.scrollarea_qwidget.setObjectName(u"scrollarea_qwidget")
        self.scrollarea_qwidget.setGeometry(QRect(0, 0, 1446, 660))
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

        self.line = QFrame(self.frame_invoice)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.frame_invoice_layout.addWidget(self.line)

        self.widget = QWidget(self.frame_invoice)
        self.widget.setObjectName(u"widget")
        self._2 = QHBoxLayout(self.widget)
        self._2.setSpacing(6)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(0, 0, 0, 0)
        self.frame_title_sub = QWidget(self.widget)
        self.frame_title_sub.setObjectName(u"frame_title_sub")
        self.frame_title_sub.setMinimumSize(QSize(250, 250))
        self.frame_title_sub.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout = QVBoxLayout(self.frame_title_sub)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_input = QLineEdit(self.frame_title_sub)
        self.title_input.setObjectName(u"title_input")
        self.title_input.setMinimumSize(QSize(250, 30))
        self.title_input.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.title_input)

        self.subheading_input = QLineEdit(self.frame_title_sub)
        self.subheading_input.setObjectName(u"subheading_input")
        self.subheading_input.setMinimumSize(QSize(250, 30))
        self.subheading_input.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.subheading_input)


        self._2.addWidget(self.frame_title_sub)

        self.frame_btn_logo = QWidget(self.widget)
        self.frame_btn_logo.setObjectName(u"frame_btn_logo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_btn_logo.sizePolicy().hasHeightForWidth())
        self.frame_btn_logo.setSizePolicy(sizePolicy1)
        self.frame_btn_logo.setMinimumSize(QSize(250, 250))
        self.frame_btn_logo.setMaximumSize(QSize(400, 250))
        self.frame_btn_logo.setBaseSize(QSize(250, 250))
        self.horizontalLayout = QHBoxLayout(self.frame_btn_logo)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.select_logo_btn = QPushButton(self.frame_btn_logo)
        self.select_logo_btn.setObjectName(u"select_logo_btn")
        sizePolicy1.setHeightForWidth(self.select_logo_btn.sizePolicy().hasHeightForWidth())
        self.select_logo_btn.setSizePolicy(sizePolicy1)
        self.select_logo_btn.setMinimumSize(QSize(250, 250))
        self.select_logo_btn.setMaximumSize(QSize(250, 250))
        self.select_logo_btn.setBaseSize(QSize(250, 250))
        self.select_logo_btn.setFont(font)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.InsertImage))
        self.select_logo_btn.setIcon(icon)
        self.select_logo_btn.setIconSize(QSize(128, 128))

        self.horizontalLayout.addWidget(self.select_logo_btn)


        self._2.addWidget(self.frame_btn_logo)

        self.frame_logo = QFrame(self.widget)
        self.frame_logo.setObjectName(u"frame_logo")
        sizePolicy1.setHeightForWidth(self.frame_logo.sizePolicy().hasHeightForWidth())
        self.frame_logo.setSizePolicy(sizePolicy1)
        self.frame_logo.setMinimumSize(QSize(250, 250))
        self.frame_logo.setMaximumSize(QSize(250, 250))
        self.frame_logo.setBaseSize(QSize(250, 250))
        self.frame_logo.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_logo)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.image_lable = QLabel(self.frame_logo)
        self.image_lable.setObjectName(u"image_lable")
        sizePolicy1.setHeightForWidth(self.image_lable.sizePolicy().hasHeightForWidth())
        self.image_lable.setSizePolicy(sizePolicy1)
        self.image_lable.setMinimumSize(QSize(250, 250))
        self.image_lable.setMaximumSize(QSize(250, 250))
        self.image_lable.setBaseSize(QSize(250, 250))

        self.verticalLayout_2.addWidget(self.image_lable)


        self._2.addWidget(self.frame_logo)

        self.frame_address = QWidget(self.widget)
        self.frame_address.setObjectName(u"frame_address")
        self.frame_address.setMinimumSize(QSize(250, 250))
        self.frame_address.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.frame_address)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.name_input = QLineEdit(self.frame_address)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setMinimumSize(QSize(250, 30))
        self.name_input.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.name_input)

        self.email_input = QLineEdit(self.frame_address)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setMinimumSize(QSize(250, 30))
        self.email_input.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.email_input)

        self.tax_number_input = QLineEdit(self.frame_address)
        self.tax_number_input.setObjectName(u"tax_number_input")
        self.tax_number_input.setMinimumSize(QSize(250, 30))
        self.tax_number_input.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.tax_number_input)

        self.phone_input = QLineEdit(self.frame_address)
        self.phone_input.setObjectName(u"phone_input")
        self.phone_input.setMinimumSize(QSize(250, 30))
        self.phone_input.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.phone_input)

        self.address_input = QLineEdit(self.frame_address)
        self.address_input.setObjectName(u"address_input")
        self.address_input.setMinimumSize(QSize(250, 30))
        self.address_input.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.address_input)

        self.country_input = QLineEdit(self.frame_address)
        self.country_input.setObjectName(u"country_input")
        self.country_input.setMinimumSize(QSize(250, 30))
        self.country_input.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.country_input)


        self._2.addWidget(self.frame_address)


        self.frame_invoice_layout.addWidget(self.widget)


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
        self.save_btn.setText(QCoreApplication.translate("Form", u"Save", None))
        self.save_btn.setProperty(u"class", QCoreApplication.translate("Form", u"primary outlined", None))
        self.label_new_invoice.setText(QCoreApplication.translate("Form", u"New Invoice", None))
        self.label_company.setText(QCoreApplication.translate("Form", u"Company", None))
        self.label_subtitle.setText(QCoreApplication.translate("Form", u"Change the address, logo, and other information for your company.", None))
        self.title_input.setPlaceholderText(QCoreApplication.translate("Form", u"Title", None))
        self.subheading_input.setPlaceholderText(QCoreApplication.translate("Form", u"Subheading", None))
        self.select_logo_btn.setText("")
        self.image_lable.setText("")
        self.name_input.setPlaceholderText(QCoreApplication.translate("Form", u"Name", None))
        self.email_input.setPlaceholderText(QCoreApplication.translate("Form", u"Email", None))
        self.tax_number_input.setPlaceholderText(QCoreApplication.translate("Form", u"Tax Number", None))
        self.phone_input.setPlaceholderText(QCoreApplication.translate("Form", u"Phone", None))
        self.address_input.setPlaceholderText(QCoreApplication.translate("Form", u"Address", None))
        self.country_input.setPlaceholderText(QCoreApplication.translate("Form", u"Country", None))
        self.label_billing.setText(QCoreApplication.translate("Form", u"Billing", None))
        self.label_advanced.setText(QCoreApplication.translate("Form", u"Advanced", None))
        Form.setTabText(Form.indexOf(self.Invoices), QCoreApplication.translate("Form", u"Page", None))
        Form.setTabText(Form.indexOf(self.Customers), QCoreApplication.translate("Form", u"Page", None))
        pass
    # retranslateUi

