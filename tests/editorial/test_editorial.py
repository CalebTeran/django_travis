from cgi import test
from http import client
from urllib import response
import pytest
from library.editorial.models import *
from rest_framework.test import APIClient
from rest_framework.test import RequestsClient

client = APIClient()

@pytest.mark.django_db
def test_editorial_name():
    editorial = Editorial.objects.create(
        name = 'Posada',
        address = 'Tizapan San Angel, Alvaro obregon',
        country = 'CDMX'
        )
    print('editorial name>>>', editorial.name)
    assert editorial.name == 'Posada'
    editorial.delete()


@pytest.mark.django_db
def test_editorial_address():
    editorial = Editorial.objects.create(
        name = 'Posada',
        address = 'Tizapan San Angel, Alvaro obregon',
        country = 'CDMX'
        )
    print('editorial adress>>>', editorial.name)
    assert editorial.address == 'Tizapan San Angel, Alvaro obregon'
    editorial.delete()


@pytest.mark.django_db
def test_editorial_country():
    editorial = Editorial.objects.create(
        name = 'Posada',
        address = 'Tizapan San Angel, Alvaro obregon',
        country = 'CDMX'
        )
    print('editorial country>>>', editorial.name)
    assert editorial.country == 'CDMX'
    editorial.delete()


@pytest.mark.django_db
def test_editorial_post_fail():
    response = client.post("editorial/company/", dict(
        nme = 'Posada',
        dress = 'Tizapan San Angel, Alvaro obregon',
        cuntr = 'CDMX'
    ))
    assert response.status_code == 404


@pytest.mark.django_db
def test_editorial_():
    payload = dict(
        name = 'Posada',
        address = 'Tizapan San Angel, Alvaro obregon',
        country = 'CDMX'
    )
    print(payload)
    response = client.post("/editorial/", payload)

    data = response.data
    assert data["name"] == payload["name"]
    assert data["address"] == payload["address"]
    assert data["country"] == payload["country"]
    assert response.status_code == 201


@pytest.mark.django_db
def test_company_phone():
    company = Company.objects.create(
        phone = '66212121',
        name = '',
        email = '',
        address = '',
        country = '',
        employees_qnt =  '',
        company_role = '',
        )
    print('company country>>>', company.phone)
    assert company.phone == '66212121'
    company.delete()


@pytest.mark.django_db
def test_company_name():
    company = Company.objects.create(
        phone = '',
        name = 'Editorial corp',
        email = '',
        address = '',
        country = '',
        employees_qnt =  '',
        company_role = '',
        )
    print('company country>>>', company.phone)
    assert company.name == 'Editorial corp'
    company.delete()


@pytest.mark.django_db
def test_company_post():
    payload = dict(
        phone = '66212121',
        name = 'Company Corp',
        address = 'nevada 123123',
        country = 'Nevada',
        employees_qnt =  '22',
        company_role = "NEWS",
    )
    print(payload)
    response = client.post("/editorial/company/", payload)
    data = response.data
    assert data["name"] == payload["name"]
    assert data["address"] == payload["address"]
    assert data["phone"] == payload["phone"]
    assert data["address"] == payload["address"]
    assert data["employees_qnt"] == payload["employees_qnt"]
    assert data["company_role"] == payload["company_role"]
    assert response.status_code == 201

@pytest.mark.django_db
def test_company_post_fail():
    response = client.post("editorial/company/", dict(
        phon = '66212121'
    ))
    assert response.status_code == 404