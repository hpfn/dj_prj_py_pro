import pytest

from certgen.core import admin
from certgen.core.admin import UserAdmin

admin_module_attr = [
    (admin, 'settings'),
    (admin, 'admin'),
    (admin, 'messages'),
    (admin, 'IS_POPUP_VAR'),
    (admin, 'unquote'),
    (admin, 'update_session_auth_hash'),
    (admin, 'sensitive_post_parameters_m'),
    (admin, 'csrf_protect_m'),
    (admin, 'AdminPasswordChangeForm'),
    (admin, 'UserChangeForm'),
    (admin, 'UserCreationForm'),
    (admin, 'PermissionDenied'),
    (admin, 'router'),
    (admin, 'transaction'),
    (admin, 'Http404'),
    (admin, 'HttpResponseRedirect'),
    (admin, 'TemplateResponse'),
    (admin, 'path'),
    (admin, 'reverse'),
    (admin, 'escape'),
    (admin, '_'),  # gettext_lazy
    (admin, 'User')
]


@pytest.mark.parametrize('a, b', admin_module_attr)
def test_admin_mod_attr(a, b):
    assert hasattr(a, b)


useradmin_class_attrs = [
    (UserAdmin, 'add_form_template'),
    (UserAdmin, 'change_user_password_template'),  # TemplateUsed test
    (UserAdmin, 'fieldsets'),
    (UserAdmin, 'add_fieldsets'),
    (UserAdmin, 'form'),
    (UserAdmin, 'add_form'),
    (UserAdmin, 'change_password_form'),
    (UserAdmin, 'list_display'),
    (UserAdmin, 'list_display'),
    (UserAdmin, 'list_filter'),
    (UserAdmin, 'search_fields'),
    (UserAdmin, 'ordering'),
    (UserAdmin, 'filter_horizontal')
]


@pytest.mark.parametrize('a, b', useradmin_class_attrs)
def test_useradmin_class_attr(a, b):
    assert hasattr(a, b)


useradmin_method_attrs = [
    (UserAdmin, 'get_fieldsets'),
    (UserAdmin, 'get_form'),
    (UserAdmin, 'get_urls'),
    (UserAdmin, 'lookup_allowed'),
    (UserAdmin, 'add_view'),
    (UserAdmin, '_add_view'),
    (UserAdmin, 'user_change_password'),
    (UserAdmin, 'response_add'),
]


@pytest.mark.parametrize('a, b', useradmin_method_attrs)
def test_useradmin_method_attr(a, b):
    assert hasattr(a, b)


def test_template_used():
    assert UserAdmin.add_form_template == 'admin/auth/user/add_form.html'


def test_profile_admin():
    assert hasattr(admin, 'ProfileAdmin')
