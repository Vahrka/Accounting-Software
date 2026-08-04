from peewee import (BooleanField, CharField, DateTimeField,
                    DeferredThroughModel, ForeignKeyField, IntegerField,
                    ManyToManyField, TextField)

from .base import BaseModelExtended, TimestampMixin


# ----- Main models (with deferred through models) -----
class Permission(BaseModelExtended):
    name = CharField(max_length=50, unique=True, index=True)
    description = TextField()

    def __str__(self):
        return self.name


class Role(BaseModelExtended):
    name = CharField(max_length=50, unique=True, index=True)
    permissions = ManyToManyField(Permission, through_model=DeferredThroughModel())

    def __str__(self):
        return self.name

    def has_permission(self, permission_name: str) -> bool:
        return self.permissions.where(Permission.name == permission_name).exists()

    def has_permissions(self, permission_names: list) -> bool:
        existing = set(p.name for p in self.permissions)
        return set(permission_names).issubset(existing)

    @classmethod
    def get_by_name(cls, name: str):
        return cls.get_or_none(cls.name == name)


class User(BaseModelExtended, TimestampMixin):
    username = CharField(max_length=50, unique=True, index=True)
    password_hash = CharField(max_length=255)
    email = CharField(max_length=100, unique=True, index=True)
    full_name = CharField(max_length=100)
    roles = ManyToManyField(Role, through_model=DeferredThroughModel())
    is_active = BooleanField(default=True)
    last_login = DateTimeField(null=True)

    class Meta:
        table_name = 'users'
        indexes = ((('username', 'email'), False),)

    def __str__(self):
        return self.username

    @classmethod
    def get_by_username(cls, username: str):
        return cls.get_or_none(username=username)

    @classmethod
    def get_by_email(cls, email: str):
        return cls.get_or_none(email=email)

    def is_authenticated(self) -> bool:
        return self.is_active

    def has_permission(self, permission_name: str) -> bool:
        for role in self.roles:
            if role.has_permission(permission_name):
                return True
        return False

    def has_permissions(self, permission_names: list) -> bool:
        if not permission_names:
            return True
        user_perms = set()
        for role in self.roles:
            for perm in role.permissions:
                user_perms.add(perm.name)
        return set(permission_names).issubset(user_perms)

    def has_role(self, role_name: str) -> bool:
        return self.roles.where(Role.name == role_name).exists()

    def authenticate(self, password: str) -> bool:
        # TODO: FIXME: hash password then check password
        return self.password_hash == password


# ----- Through tables (defined after the main models) -----
class RolePermission(BaseModelExtended):
    role = ForeignKeyField(Role, backref='role_permissions')
    permission = ForeignKeyField(Permission, backref='permission_roles')


class UserRole(BaseModelExtended):
    user = ForeignKeyField(User, backref='user_roles')
    role = ForeignKeyField(Role, backref='role_users')


# ----- Now assign the real through models to the ManyToMany fields -----
Role.permissions.through_model = RolePermission
User.roles.through_model = UserRole
