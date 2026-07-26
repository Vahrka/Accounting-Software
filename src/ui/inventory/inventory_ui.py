# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inventory.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDoubleSpinBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QTableView,
    QVBoxLayout, QWidget)
import source_rc

class Ui_Inventory(object):
    def setupUi(self, Inventory):
        if not Inventory.objectName():
            Inventory.setObjectName(u"Inventory")
        Inventory.resize(1117, 877)
        self.Items = QWidget()
        self.Items.setObjectName(u"Items")
        self.items_base_layout = QVBoxLayout(self.Items)
        self.items_base_layout.setObjectName(u"items_base_layout")
        self.items_toolbar_layout = QHBoxLayout()
        self.items_toolbar_layout.setObjectName(u"items_toolbar_layout")
        self.item_search_input = QLineEdit(self.Items)
        self.item_search_input.setObjectName(u"item_search_input")

        self.items_toolbar_layout.addWidget(self.item_search_input)

        self.item_category_filter = QComboBox(self.Items)
        self.item_category_filter.setObjectName(u"item_category_filter")
        self.item_category_filter.setEditable(False)

        self.items_toolbar_layout.addWidget(self.item_category_filter)

        self.add_item_btn = QPushButton(self.Items)
        self.add_item_btn.setObjectName(u"add_item_btn")

        self.items_toolbar_layout.addWidget(self.add_item_btn)


        self.items_base_layout.addLayout(self.items_toolbar_layout)

        self.items_table_view = QTableView(self.Items)
        self.items_table_view.setObjectName(u"items_table_view")
        self.items_table_view.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.items_table_view.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.items_table_view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.items_table_view.setSortingEnabled(True)

        self.items_base_layout.addWidget(self.items_table_view)

        self.item_form_scroll_area = QScrollArea(self.Items)
        self.item_form_scroll_area.setObjectName(u"item_form_scroll_area")
        self.item_form_scroll_area.setWidgetResizable(True)
        self.item_form_scrollarea_widget = QWidget()
        self.item_form_scrollarea_widget.setObjectName(u"item_form_scrollarea_widget")
        self.item_form_scrollarea_widget.setGeometry(QRect(0, 0, 1093, 391))
        self.item_form_layout = QVBoxLayout(self.item_form_scrollarea_widget)
        self.item_form_layout.setObjectName(u"item_form_layout")
        self.item_form_label = QLabel(self.item_form_scrollarea_widget)
        self.item_form_label.setObjectName(u"item_form_label")

        self.item_form_layout.addWidget(self.item_form_label)

        self.item_form_row_1 = QHBoxLayout()
        self.item_form_row_1.setObjectName(u"item_form_row_1")
        self.sku_input = QLineEdit(self.item_form_scrollarea_widget)
        self.sku_input.setObjectName(u"sku_input")

        self.item_form_row_1.addWidget(self.sku_input)

        self.name_input = QLineEdit(self.item_form_scrollarea_widget)
        self.name_input.setObjectName(u"name_input")

        self.item_form_row_1.addWidget(self.name_input)

        self.category_input = QComboBox(self.item_form_scrollarea_widget)
        self.category_input.setObjectName(u"category_input")
        self.category_input.setEditable(True)

        self.item_form_row_1.addWidget(self.category_input)

        self.supplier_input = QComboBox(self.item_form_scrollarea_widget)
        self.supplier_input.setObjectName(u"supplier_input")
        self.supplier_input.setEditable(False)

        self.item_form_row_1.addWidget(self.supplier_input)


        self.item_form_layout.addLayout(self.item_form_row_1)

        self.item_form_row_2 = QHBoxLayout()
        self.item_form_row_2.setObjectName(u"item_form_row_2")
        self.unit_price_input = QDoubleSpinBox(self.item_form_scrollarea_widget)
        self.unit_price_input.setObjectName(u"unit_price_input")
        self.unit_price_input.setMaximum(1000000.000000000000000)

        self.item_form_row_2.addWidget(self.unit_price_input)

        self.cost_price_input = QDoubleSpinBox(self.item_form_scrollarea_widget)
        self.cost_price_input.setObjectName(u"cost_price_input")
        self.cost_price_input.setMaximum(1000000.000000000000000)

        self.item_form_row_2.addWidget(self.cost_price_input)

        self.stock_quantity_input = QSpinBox(self.item_form_scrollarea_widget)
        self.stock_quantity_input.setObjectName(u"stock_quantity_input")
        self.stock_quantity_input.setMaximum(1000000)

        self.item_form_row_2.addWidget(self.stock_quantity_input)

        self.reorder_level_input = QSpinBox(self.item_form_scrollarea_widget)
        self.reorder_level_input.setObjectName(u"reorder_level_input")
        self.reorder_level_input.setMaximum(1000000)

        self.item_form_row_2.addWidget(self.reorder_level_input)

        self.location_input = QLineEdit(self.item_form_scrollarea_widget)
        self.location_input.setObjectName(u"location_input")

        self.item_form_row_2.addWidget(self.location_input)


        self.item_form_layout.addLayout(self.item_form_row_2)

        self.description_input = QPlainTextEdit(self.item_form_scrollarea_widget)
        self.description_input.setObjectName(u"description_input")
        self.description_input.setMaximumSize(QSize(16777215, 80))

        self.item_form_layout.addWidget(self.description_input)

        self.item_form_actions_layout = QHBoxLayout()
        self.item_form_actions_layout.setObjectName(u"item_form_actions_layout")
        self.save_item_btn = QPushButton(self.item_form_scrollarea_widget)
        self.save_item_btn.setObjectName(u"save_item_btn")

        self.item_form_actions_layout.addWidget(self.save_item_btn)

        self.delete_item_btn = QPushButton(self.item_form_scrollarea_widget)
        self.delete_item_btn.setObjectName(u"delete_item_btn")

        self.item_form_actions_layout.addWidget(self.delete_item_btn)

        self.clear_item_btn = QPushButton(self.item_form_scrollarea_widget)
        self.clear_item_btn.setObjectName(u"clear_item_btn")

        self.item_form_actions_layout.addWidget(self.clear_item_btn)

        self.item_form_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.item_form_actions_layout.addItem(self.item_form_spacer)


        self.item_form_layout.addLayout(self.item_form_actions_layout)

        self.item_form_scroll_area.setWidget(self.item_form_scrollarea_widget)

        self.items_base_layout.addWidget(self.item_form_scroll_area)

        Inventory.addTab(self.Items, "")
        self.Suppliers = QWidget()
        self.Suppliers.setObjectName(u"Suppliers")
        self.suppliers_base_layout = QVBoxLayout(self.Suppliers)
        self.suppliers_base_layout.setObjectName(u"suppliers_base_layout")
        self.suppliers_toolbar_layout = QHBoxLayout()
        self.suppliers_toolbar_layout.setObjectName(u"suppliers_toolbar_layout")
        self.supplier_search_input = QLineEdit(self.Suppliers)
        self.supplier_search_input.setObjectName(u"supplier_search_input")

        self.suppliers_toolbar_layout.addWidget(self.supplier_search_input)

        self.add_supplier_btn = QPushButton(self.Suppliers)
        self.add_supplier_btn.setObjectName(u"add_supplier_btn")

        self.suppliers_toolbar_layout.addWidget(self.add_supplier_btn)


        self.suppliers_base_layout.addLayout(self.suppliers_toolbar_layout)

        self.suppliers_table_view = QTableView(self.Suppliers)
        self.suppliers_table_view.setObjectName(u"suppliers_table_view")
        self.suppliers_table_view.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.suppliers_table_view.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.suppliers_table_view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.suppliers_table_view.setSortingEnabled(True)

        self.suppliers_base_layout.addWidget(self.suppliers_table_view)

        self.supplier_form_layout = QVBoxLayout()
        self.supplier_form_layout.setObjectName(u"supplier_form_layout")
        self.supplier_form_label = QLabel(self.Suppliers)
        self.supplier_form_label.setObjectName(u"supplier_form_label")

        self.supplier_form_layout.addWidget(self.supplier_form_label)

        self.supplier_form_row_1 = QHBoxLayout()
        self.supplier_form_row_1.setObjectName(u"supplier_form_row_1")
        self.supplier_name_input = QLineEdit(self.Suppliers)
        self.supplier_name_input.setObjectName(u"supplier_name_input")

        self.supplier_form_row_1.addWidget(self.supplier_name_input)

        self.contact_person_input = QLineEdit(self.Suppliers)
        self.contact_person_input.setObjectName(u"contact_person_input")

        self.supplier_form_row_1.addWidget(self.contact_person_input)

        self.supplier_email_input = QLineEdit(self.Suppliers)
        self.supplier_email_input.setObjectName(u"supplier_email_input")

        self.supplier_form_row_1.addWidget(self.supplier_email_input)

        self.supplier_phone_input = QLineEdit(self.Suppliers)
        self.supplier_phone_input.setObjectName(u"supplier_phone_input")

        self.supplier_form_row_1.addWidget(self.supplier_phone_input)


        self.supplier_form_layout.addLayout(self.supplier_form_row_1)

        self.supplier_address_input = QLineEdit(self.Suppliers)
        self.supplier_address_input.setObjectName(u"supplier_address_input")

        self.supplier_form_layout.addWidget(self.supplier_address_input)

        self.supplier_form_actions_layout = QHBoxLayout()
        self.supplier_form_actions_layout.setObjectName(u"supplier_form_actions_layout")
        self.save_supplier_btn = QPushButton(self.Suppliers)
        self.save_supplier_btn.setObjectName(u"save_supplier_btn")

        self.supplier_form_actions_layout.addWidget(self.save_supplier_btn)

        self.delete_supplier_btn = QPushButton(self.Suppliers)
        self.delete_supplier_btn.setObjectName(u"delete_supplier_btn")

        self.supplier_form_actions_layout.addWidget(self.delete_supplier_btn)

        self.clear_supplier_btn = QPushButton(self.Suppliers)
        self.clear_supplier_btn.setObjectName(u"clear_supplier_btn")

        self.supplier_form_actions_layout.addWidget(self.clear_supplier_btn)

        self.supplier_form_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.supplier_form_actions_layout.addItem(self.supplier_form_spacer)


        self.supplier_form_layout.addLayout(self.supplier_form_actions_layout)


        self.suppliers_base_layout.addLayout(self.supplier_form_layout)

        Inventory.addTab(self.Suppliers, "")

        self.retranslateUi(Inventory)

        Inventory.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Inventory)
    # setupUi

    def retranslateUi(self, Inventory):
        self.item_search_input.setPlaceholderText(QCoreApplication.translate("Inventory", u"Search by SKU or name", None))
        self.add_item_btn.setText(QCoreApplication.translate("Inventory", u"New Item", None))
        self.add_item_btn.setProperty(u"class", QCoreApplication.translate("Inventory", u"primary outlined", None))
        self.item_form_label.setText(QCoreApplication.translate("Inventory", u"Item Details", None))
        self.sku_input.setPlaceholderText(QCoreApplication.translate("Inventory", u"SKU", None))
        self.name_input.setPlaceholderText(QCoreApplication.translate("Inventory", u"Name", None))
        self.unit_price_input.setPrefix(QCoreApplication.translate("Inventory", u"Price: ", None))
        self.cost_price_input.setPrefix(QCoreApplication.translate("Inventory", u"Cost: ", None))
        self.stock_quantity_input.setPrefix(QCoreApplication.translate("Inventory", u"Stock: ", None))
        self.reorder_level_input.setPrefix(QCoreApplication.translate("Inventory", u"Reorder at: ", None))
        self.location_input.setPlaceholderText(QCoreApplication.translate("Inventory", u"Location", None))
        self.description_input.setPlaceholderText(QCoreApplication.translate("Inventory", u"Description", None))
        self.save_item_btn.setText(QCoreApplication.translate("Inventory", u"Save Item", None))
        self.save_item_btn.setProperty(u"class", QCoreApplication.translate("Inventory", u"primary outlined", None))
        self.delete_item_btn.setText(QCoreApplication.translate("Inventory", u"Delete", None))
        self.clear_item_btn.setText(QCoreApplication.translate("Inventory", u"Clear", None))
        Inventory.setTabText(Inventory.indexOf(self.Items), QCoreApplication.translate("Inventory", u"Items", None))
        self.supplier_search_input.setPlaceholderText(QCoreApplication.translate("Inventory", u"Search suppliers", None))
        self.add_supplier_btn.setText(QCoreApplication.translate("Inventory", u"New Supplier", None))
        self.add_supplier_btn.setProperty(u"class", QCoreApplication.translate("Inventory", u"primary outlined", None))
        self.supplier_form_label.setText(QCoreApplication.translate("Inventory", u"Supplier Details", None))
        self.supplier_name_input.setPlaceholderText(QCoreApplication.translate("Inventory", u"Name", None))
        self.contact_person_input.setPlaceholderText(QCoreApplication.translate("Inventory", u"Contact Person", None))
        self.supplier_email_input.setPlaceholderText(QCoreApplication.translate("Inventory", u"Email", None))
        self.supplier_phone_input.setPlaceholderText(QCoreApplication.translate("Inventory", u"Phone", None))
        self.supplier_address_input.setPlaceholderText(QCoreApplication.translate("Inventory", u"Address", None))
        self.save_supplier_btn.setText(QCoreApplication.translate("Inventory", u"Save Supplier", None))
        self.save_supplier_btn.setProperty(u"class", QCoreApplication.translate("Inventory", u"primary outlined", None))
        self.delete_supplier_btn.setText(QCoreApplication.translate("Inventory", u"Delete", None))
        self.clear_supplier_btn.setText(QCoreApplication.translate("Inventory", u"Clear", None))
        Inventory.setTabText(Inventory.indexOf(self.Suppliers), QCoreApplication.translate("Inventory", u"Suppliers", None))
        pass
    # retranslateUi

