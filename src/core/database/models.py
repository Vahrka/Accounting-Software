from pathlib import Path

from peewee import (CharField, DateField, DecimalField, ForeignKeyField, Model,
                    SqliteDatabase, TextField)

# Initialize database
db = SqliteDatabase(None)  # Path will be set later


class BaseModel(Model):
    class Meta:
        database = db


class Account(BaseModel):
    """Represents an account in the general ledger"""
    name = CharField(unique=True)
    description = TextField(null=True)
    balance = DecimalField(default=0.0, decimal_places=2)


class Transaction(BaseModel):
    """Represents a financial transaction"""
    date = DateField()
    description = CharField()
    amount = DecimalField(decimal_places=2)
    from_account = ForeignKeyField(Account, backref='outgoing_transactions')
    to_account = ForeignKeyField(Account, backref='incoming_transactions')


class Billing(BaseModel):
    """Billings"""
    name = CharField(max_length=50)
    price = DecimalField()
    count = DecimalField()


def initialize_database(db_path: Path):
    """Initialize the database and create tables"""
    db.init(db_path)
    db.connect()
    db.create_tables([Account, Transaction, Billing], safe=True)
    return db.close()
