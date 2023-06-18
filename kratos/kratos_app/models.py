from django.db import models


# Create your models here.
class Producer(models.Model):
    producer = models.CharField('Производитель', max_length=50)

    def __str__(self):
        return self.producer

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

class Category(models.Model):
    category = models.CharField('Категория', max_length=50)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Component(models.Model):
    image = models.ImageField(null=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField('Модель', max_length=100)
    producer = models.ForeignKey('Producer', on_delete=models.PROTECT, null=True, blank=True)
    release_year = models.PositiveIntegerField('Год релиза')
    description = models.CharField('Описание', max_length=500)
    characteristic = models.CharField('Характеристики', max_length=3000)
    price = models.PositiveIntegerField('Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


