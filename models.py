from django.db import models


class Seller(models.Model):
    company_name = models.CharField(max_length=50, verbose_name='Название компании')
    phone = models.CharField(max_length=50, verbose_name='Номер телефона')
    adress = models.CharField(max_length=50, verbose_name='Адрес')

    object = models.Manager


class Customer(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя покупателя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    phone = models.CharField(max_length=50, verbose_name='Номер телефона')

    object = models.Manager

# Create your models here.
