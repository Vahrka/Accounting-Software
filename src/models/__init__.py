from utils.logger import get_logger

from .account import Account
from .base import BaseModelExtended, SoftDeleteMixin, TimestampMixin
from .customer import Customer
from .database import BaseModel, _db, db_manager, init_database
from .employee import Employee
from .inventory_item import InventoryItem, Supplier
from .invoice import Invoice
from .sales import Billing, Sale, SaleItem
from .transaction import Transaction
from .user import Permission, Role, RolePermission, User, UserRole

logger = get_logger()

# List all models for table creation
ALL_MODELS = [
    User,
    Permission,
    Role,
    RolePermission,
    UserRole,
    Account,
    Employee,
    Customer,
    InventoryItem,
    Sale,
    SaleItem,
    Supplier,
    Invoice,
    Transaction,
    Billing,
]


def create_tables() -> None:
    """Create all tables if they don't exist"""
    _db.create_tables(ALL_MODELS, safe=True)


def drop_tables() -> None:
    """Drop all tables (use with caution)"""
    _db.drop_tables(ALL_MODELS, safe=True)


def initialize_test_data() -> None:
    """Initialize test data for development (idempotent)"""
    # Get or create default permissions
    perm_view_users, _ = Permission.get_or_create(
        name='view_users',
        defaults={'description': 'Can view user list'}
    )
    perm_edit_users, _ = Permission.get_or_create(
        name='edit_users',
        defaults={'description': 'Can edit users'}
    )
    perm_view_reports, _ = Permission.get_or_create(
        name='view_reports',
        defaults={'description': 'Can view reports'}
    )

    # Get or create default roles
    admin_role, _ = Role.get_or_create(name='admin')
    manager_role, _ = Role.get_or_create(name='manager')

    # Assign permissions to roles using the explicit through model
    # (this is idempotent and avoids the .add() method issues)
    for role, perms in [
        (admin_role, [perm_view_users, perm_edit_users, perm_view_reports]),
        (manager_role, [perm_view_users, perm_view_reports]),
    ]:
        for perm in perms:
            RolePermission.get_or_create(role=role, permission=perm)

    # Create admin user only if no users exist
    if User.select().count() == 0:
        admin = User.create(
            username='admin',
            email='admin@example.com',
            password_hash='hashed_password',   # replace with proper hashing later
            full_name='Administrator',
            is_active=True
        )
        # Assign admin role to user using the explicit through model
        UserRole.get_or_create(user=admin, role=admin_role)

        # Create sample customer
        customer, _ = Customer.get_or_create(
            email='john@example.com',
            defaults={
                'name': 'John Doe',
                'phone': '123-456-7890',
                'address': '123 Main St',
                'city': 'New York',
                'state': 'NY',
                'country': 'USA',
                'postal_code': '10001',
                'created_by': admin
            }
        )
        logger.info("Test data created successfully!")
    else:
        logger.info("Test data already exists, skipping creation.")


# What to export
__all__ = [
    # Database
    'BaseModel',
    'init_database',
    'db_manager',
    '_db',

    # Base utilities
    'BaseModelExtended',
    'TimestampMixin',
    'SoftDeleteMixin',

    # Models
    'User',
    'Permission',
    'Role',
    'RolePermission',
    'UserRole',
    'Account',
    'Employee',
    'Customer',
    'InventoryItem',
    'Supplier',
    'Sale',
    'SaleItem',
    'Invoice',
    'Transaction',
    'Billing',

    # Utilities
    'ALL_MODELS',
    'create_tables',
    'drop_tables',
    'initialize_test_data',
]
