from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Editorial(models.Model):
	name = models.CharField(max_length=128)
	address = models.CharField(max_length=128)
	country = models.CharField(max_length=128)


class Company(models.Model):
	
    class CompanyRoles(models.TextChoices):
        BOOKS = 'BOOKS', _('Books')
        MAGAZINE = 'MAGAZINE', _('Magazine')
        NEWS = 'NEWS', _('News')
        MANGA = 'MANGA', _('Manga')
        COMICS = 'COMICS', _('Comics')

    phone = models.CharField(max_length=12)
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    address = models.CharField(max_length=254)
    country = models.CharField(max_length=128)
    employees_qnt = models.CharField(max_length=12) 
    company_role = models.CharField(max_length=24, choices=CompanyRoles.choices, default=CompanyRoles.BOOKS )