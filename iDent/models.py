from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Main(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=50)
    image = models.ImageField(verbose_name='Фото')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(verbose_name='Категории', max_length=50)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50)
    text = models.CharField(verbose_name='Описание', max_length=255)
    image = models.ImageField(verbose_name='Фото')

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=50)
    text = models.TextField(verbose_name='Текст', max_length=255)
    image = models.ImageField(verbose_name='Фото')

    def __str__(self):
        return self.title


class Company(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=50)
    text = models.TextField(verbose_name='Текст', max_length=255)

    def __str__(self):
        return self.title


class Address(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50)
    address = models.CharField(verbose_name='Адрес', max_length=255)
    main_place = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Contact(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50)
    address = models.CharField(verbose_name='Адрес', max_length=50)
    numbers = PhoneNumberField(region='KG', verbose_name=255)
    email = models.EmailField(verbose_name='Электронная почта', blank=True)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(verbose_name='Новости', max_length=50)
    description = models.TextField(verbose_name='Описание', default='')
    image = models.ImageField(upload_to='Новости', verbose_name='Фото')
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False, verbose_name='Актуально')

    def __str__(self):
        return self.title


class Banner(models.Model):
    title = models.CharField(verbose_name='Описание', max_length=255)
    text = models.TextField(verbose_name='Текст', max_length=255)
    image = models.ImageField(verbose_name='Фото')

    def __str__(self):
        return self.title


class Swipers(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=50)
    text = models.TextField(verbose_name='Текст', max_length=255)
    image = models.ImageField(verbose_name='Фото')

    def __str__(self):
        return self.title


class Icons(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=50)
    image = models.FileField(verbose_name='Фото', default='')

    def __str__(self):
        return self.title


class Details(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50)
    description = models.TextField(verbose_name='Описание', default='')

    def __str__(self):
        return self.title


class Pictures(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=50)
    description = models.TextField(verbose_name='Текст',default='')
    image = models.ImageField(verbose_name='Фото', default='')

    def __str__(self):
        return self.title


class Link(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50)
    text = models.TextField(verbose_name='Заголовок', max_length=255)
    image = models.ImageField(verbose_name='Фото')
    url = models.URLField(verbose_name='')

    def __str__(self):
        return self.title


class Splitted(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=50)
    text = models.TextField(verbose_name='Текст', max_length=255)
    image = models.ImageField(verbose_name='Фото', default='')

    def __str__(self):
        return self.title


class Footer(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50)
    text = models.TextField(verbose_name='Заголовок', max_length=50)
    image = models.FileField(verbose_name='Значки', default='')

    def __str__(self):
        return self.title




