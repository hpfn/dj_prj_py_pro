import pytest
from django.contrib.auth.base_user import BaseUserManager

from certgen.core import managers
from certgen.core.managers import UserManager


# module attr
def test_managers_import():
    assert hasattr(managers, 'BaseUserManager')


def test_usermanager_subclass():
    assert issubclass(UserManager, BaseUserManager)


class_attrs = [
    (UserManager, 'use_in_migrations'),  # class attr
    (UserManager, '_create_user'),
    (UserManager, 'create_user'),
    (UserManager, 'create_superuser')
]


@pytest.mark.parametrize('a, b', class_attrs)
def test_usermanager_attrs(a, b):
    assert hasattr(a, b)
