# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_language.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import source_rc

class Ui_LanguageSetting(object):
    def setupUi(self, LanguageSetting):
        if not LanguageSetting.objectName():
            LanguageSetting.setObjectName(u"LanguageSetting")
        LanguageSetting.resize(800, 574)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LanguageSetting.sizePolicy().hasHeightForWidth())
        LanguageSetting.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(LanguageSetting)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(LanguageSetting)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignTop)

        self.language_input = QComboBox(self.widget)
        self.language_input.addItem("")
        self.language_input.addItem("")
        self.language_input.setObjectName(u"language_input")

        self.horizontalLayout.addWidget(self.language_input, 0, Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 10)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.font_input = QComboBox(self.widget)
        self.font_input.setObjectName(u"font_input")
        self.font_input.setMaxVisibleItems(5)
        self.font_input.setMaxCount(5)

        self.horizontalLayout_3.addWidget(self.font_input)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 10)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_2.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.save_btn = QPushButton(LanguageSetting)
        self.save_btn.setObjectName(u"save_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy1)
        self.save_btn.setMinimumSize(QSize(150, 0))
        icon = QIcon()
        icon.addFile(u":/icons/save-storage-file-document", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.save_btn.setIcon(icon)
        self.save_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.save_btn, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 2)

        self.retranslateUi(LanguageSetting)

        self.font_input.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(LanguageSetting)
    # setupUi

    def retranslateUi(self, LanguageSetting):
        LanguageSetting.setWindowTitle(QCoreApplication.translate("LanguageSetting", u"Language Settings", None))
        self.label.setText(QCoreApplication.translate("LanguageSetting", u"Language:", None))
        self.language_input.setItemText(0, QCoreApplication.translate("LanguageSetting", u"English (English)", None))
        self.language_input.setItemText(1, QCoreApplication.translate("LanguageSetting", u"Persian (\u067e\u0627\u0631\u0633\u06cc)", None))

        self.label_2.setText(QCoreApplication.translate("LanguageSetting", u"Font:", None))
        self.save_btn.setText(QCoreApplication.translate("LanguageSetting", u"Save", None))
    # retranslateUi

