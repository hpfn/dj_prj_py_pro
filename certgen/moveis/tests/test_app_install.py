from certgen.moveis import apps
from certgen import settings


def test_appconfig_name():
    assert apps.MoveisConfig.name == 'certgen.moveis'


def test_app_in_settings():
    assert 'certgen.moveis' in settings.INSTALLED_APPS
