from os import path

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile

from certgen.moveis.models import Movel

attrs = [
    (Movel, 'titulo'),
    (Movel, 'preco'),
    (Movel, 'descricao'),
    (Movel, 'foto'),
]


@pytest.mark.parametrize('a, b', attrs)
def test_movel_attrs(a, b):
    assert hasattr(a, b)


IMAGE_PATH = path.dirname(__file__)
IMAGE_PATH = path.join(IMAGE_PATH, 'prensa.jpg')


@pytest.fixture
def test_save_in_db(db):
    image = SimpleUploadedFile(
        name='prensa.jpg',
        content=open(IMAGE_PATH, 'rb').read(),
        content_type='image/jpeg'
    )
    return Movel.objects.create(
        titulo='Prensa',
        preco='300.00',
        foto=image,
        descricao='Prensa de farinha'
    )


def test_db_info(test_save_in_db):
    one_item = Movel.objects.all().count()
    assert one_item == 1
