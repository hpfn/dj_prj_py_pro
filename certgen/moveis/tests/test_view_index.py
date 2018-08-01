import pytest
from django.shortcuts import reverse as r
from certgen.django_assertions import dj_assert_template_used


@pytest.fixture
def client_get_resp(client, db):
    return client.get(r('moveis:index'))


def test_get_index_page(client_get_resp):
    resp = client_get_resp
    assert 200 == resp.status_code


def test_template_used(client_get_resp):
    resp = client_get_resp
    dj_assert_template_used(resp, 'moveis/index.html')


def test_context_key(client_get_resp):
    resp = client_get_resp
    assert 'categorias' in resp.context
