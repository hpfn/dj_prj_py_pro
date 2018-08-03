import pytest

from certgen.core.models import User, Profile

inst_params = [
    (Profile, 'nome_completo'),
    (Profile, 'usuario')

]


@pytest.mark.parametrize('a, b', inst_params)
def test_attrs(a, b):
    assert hasattr(a, b)


def test_create_profile(django_user_model):
    user = User.objects.create(email='teste@teste.com', password='12345678')
    Profile.objects.create(nome_completo='teste de criacao', usuario=user)
    assert Profile.objects.get(nome_completo='teste de criacao')
