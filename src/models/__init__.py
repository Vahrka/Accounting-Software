from utils.logger import get_logger

# Base & database
from .base import BaseModelExtended, SoftDeleteMixin, TimestampMixin
from .database import BaseModel, _db, db_manager, init_database

# Security & users
from .user import (Permission, Role, RolePermission, User, UserRole)

# Core accounting
from .account import ACCOUNT_TYPES, LedgerAccount
from .currency import Currency
from .tax import TAX_TYPES, Tax
from .transaction import (JournalTransaction, PaymentTransaction,
                          TransactionEntry)
from .financial_report import FILE_FORMATS, FinancialReport, REPORT_TYPES

# Business
from .customer import Customer
from .employee import Employee
from .inventory_item import Category, InventoryItem, Supplier
from .invoice import INVOICE_STATUSES, Invoice
from .invoice_line import InvoiceLine
from .sales import Billing, Sale, SaleItem
from .receipt import RECEIPT_STATUSES, Receipt
from .payroll import (DEDUCTION_TYPES, EARNING_TYPES, PAYROLL_STATUSES,
                      PAY_TYPES, Payroll, PayrollDeduction, PayrollEarning)

# Banking
from .bank_feed import (BankAccount, BankFeed, BankTransaction,
                        Reconciliation, ReconciliationItem)

# Technical
from .backup import BACKUP_STATUSES, Backup
from .theme import Theme
from .system_settings import SystemSettings

logger = get_logger()

# Ordered so that foreign-key dependencies are satisfied
ALL_MODELS = [
    # Security
    Permission,
    Role,
    RolePermission,
    UserRole,
    User,
    # Core accounting
    Currency,
    Tax,
    LedgerAccount,
    JournalTransaction,
    TransactionEntry,
    PaymentTransaction,
    FinancialReport,
    # Business
    Customer,
    Supplier,
    Category,
    InventoryItem,
    Invoice,
    InvoiceLine,
    Sale,
    SaleItem,
    Billing,
    Receipt,
    Employee,
    Payroll,
    PayrollDeduction,
    PayrollEarning,
    # Banking
    BankAccount,
    BankFeed,
    BankTransaction,
    Reconciliation,
    ReconciliationItem,
    # Technical
    Backup,
    Theme,
    SystemSettings,
]


def create_tables() -> None:
    """Create all tables if they don't exist."""
    _db.create_tables(ALL_MODELS, safe=True)


def drop_tables() -> None:
    """Drop all tables (use with caution)."""
    _db.drop_tables(ALL_MODELS, safe=True)


def initialize_test_data() -> None:
    """Seed default permissions, roles, currencies, and admin user."""
    from decimal import Decimal

    # --- Permissions ---
    perms_data = [
        ('view_users', 'Can view user list'),
        ('edit_users', 'Can edit / create users'),
        ('delete_users', 'Can delete users'),
        ('view_invoices', 'Can view invoices'),
        ('create_invoices', 'Can create invoices'),
        ('edit_invoices', 'Can edit invoices'),
        ('delete_invoices', 'Can delete invoices'),
        ('view_accounts', 'Can view chart of accounts'),
        ('edit_accounts', 'Can create / edit accounts'),
        ('post_transactions', 'Can post journal entries'),
        ('view_reports', 'Can view financial reports'),
        ('generate_reports', 'Can generate / export reports'),
        ('manage_inventory', 'Can manage inventory items'),
        ('manage_payroll', 'Can manage payroll'),
        ('manage_banking', 'Can manage bank feeds & reconciliation'),
        ('manage_settings', 'Can change system settings'),
        ('view_dashboard', 'Can view the dashboard'),
    ]
    perm_objs = []
    for name, desc in perms_data:
        p, _ = Permission.get_or_create(
            name=name, defaults={'description': desc},
        )
        perm_objs.append(p)

    # --- Roles ---
    admin_perms = perm_objs  # admin gets everything
    accountant_perms = [p for p in perm_objs if p.name in (
        'view_invoices', 'create_invoices', 'edit_invoices',
        'view_accounts', 'post_transactions',
        'view_reports', 'generate_reports',
        'manage_inventory', 'manage_banking', 'view_dashboard',
    )]
    viewer_perms = [p for p in perm_objs if p.name in (
        'view_invoices', 'view_accounts', 'view_reports', 'view_dashboard',
    )]

    roles_map = {
        'admin': admin_perms,
        'accountant': accountant_perms,
        'viewer': viewer_perms,
    }
    role_objs = {}
    for role_name, perms in roles_map.items():
        role, _ = Role.get_or_create(name=role_name)
        role_objs[role_name] = role
        for perm in perms:
            RolePermission.get_or_create(role=role, permission=perm)

    # --- Currencies ---
    currencies = [
        ('USD', 'US Dollar', '$', Decimal('1.000000'), True),
        ('EUR', 'Euro', '€', Decimal('0.920000'), False),
        ('GBP', 'British Pound', '£', Decimal('0.790000'), False),
        ('IRR', 'Iranian Rial', '﷼', Decimal('420000.000000'), False),
    ]
    for code, name, symbol, rate, is_base in currencies:
        Currency.get_or_create(
            code=code,
            defaults={
                'name': name,
                'symbol': symbol,
                'exchange_rate': rate,
                'is_base': is_base,
            },
        )

    # --- Default tax ---
    Tax.get_or_create(
        name='Default VAT',
        defaults={'rate': Decimal('9.0000'), 'is_default': True},
    )

    # --- Admin user ---
    if User.select().count() == 0:
        admin = User.create(
            username='admin',
            email='admin@example.com',
            password_hash='hashed_password',
            full_name='Administrator',
            is_active=True,
        )
        UserRole.get_or_create(
            user=admin, role=role_objs['admin'],
        )

        # Sample customer
        Customer.get_or_create(
            email='john@example.com',
            defaults={
                'name': 'John Doe',
                'phone': '123-456-7890',
                'address': '123 Main St',
                'city': 'Tehran',
                'state': 'Tehran',
                'country': 'Iran',
                'postal_code': '1234567890',
                'created_by': admin,
            },
        )
        logger.info("Test data created successfully!")
    else:
        logger.info("Test data already exists, skipping creation.")


__all__ = [
    # Database
    'BaseModel', 'init_database', 'db_manager', '_db',
    # Base utilities
    'BaseModelExtended', 'TimestampMixin', 'SoftDeleteMixin',
    # Security
    'User', 'Permission', 'Role', 'RolePermission', 'UserRole',
    # Core accounting
    'Currency', 'Tax', 'LedgerAccount', 'ACCOUNT_TYPES',
    'JournalTransaction', 'TransactionEntry', 'PaymentTransaction',
    'FinancialReport', 'REPORT_TYPES', 'FILE_FORMATS',
    # Business
    'Customer', 'Supplier', 'Category', 'InventoryItem',
    'Invoice', 'INVOICE_STATUSES', 'InvoiceLine',
    'Sale', 'SaleItem', 'Billing',
    'Receipt', 'RECEIPT_STATUSES',
    'Employee',
    'Payroll', 'PAYROLL_STATUSES', 'PAY_TYPES',
    'PayrollDeduction', 'DEDUCTION_TYPES',
    'PayrollEarning', 'EARNING_TYPES',
    # Banking
    'BankAccount', 'BankFeed', 'BankTransaction',
    'Reconciliation', 'ReconciliationItem',
    # Technical
    'Backup', 'BACKUP_STATUSES',
    'Theme', 'SystemSettings',
    # Utilities
    'ALL_MODELS', 'create_tables', 'drop_tables', 'initialize_test_data',
]
