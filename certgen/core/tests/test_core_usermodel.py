import pytest
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import IntegrityError

from certgen.core import models
from certgen.core.models import User

model_module_attr = [
    (models, 'send_mail'),
    (models, 'models'),
    (models, 'AbstractBaseUser'),
    (models, 'PermissionsMixin'),
    (models, 'timezone'),
    (models, '_'),  # gettext_lazy as
    (models, 'UserManager')
]


@pytest.mark.parametrize('a, b', model_module_attr)
def test_base_user_manager_import(a, b):
    assert hasattr(a, b)


subclass_inherit = [
    (User, AbstractBaseUser),
    (User, PermissionsMixin)
]


@pytest.mark.parametrize('a, b', subclass_inherit)
def test_usermanager_subclass(a, b):
    assert issubclass(a, b)


class_attrs = [
    (User, 'name'),
    (User, 'email'),
    (User, 'is_staff'),
    (User, 'is_active'),
    (User, 'date_joined'),
    (User, 'EMAIL_FIELD'),
    (User, 'USERNAME_FIELD'),
    (User, 'REQUIRED_FIELDS'),
    (User, 'clean'),
    (User, 'get_full_name'),
    (User, 'get_short_name'),
    (User, 'email_user'),
]


@pytest.mark.parametrize('a, b', class_attrs)
def test_usermanager_attrs(a, b):
    assert hasattr(a, b)


def test_username_field():
    usr = User()
    assert usr.USERNAME_FIELD == 'email'


def test_get_name():
    usr = User()
    assert usr.get_full_name() == usr.get_short_name()


def test_unique_email(django_user_model):
    usr = User()
    usr.name = 'Jose'
    usr.email = 'jose@email.com'

    usr1 = User()
    usr1.name = 'Jose'
    usr1.email = 'jose@email.com'

    with pytest.raises(IntegrityError):
        usr.save()
        usr1.save()


def test_auth_user_model():
    assert settings.AUTH_USER_MODEL == 'core.User'

# send_email test?
