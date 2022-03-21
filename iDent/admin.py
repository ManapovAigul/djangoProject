from django.contrib import admin
from .models import *

admin.site.register([Main, Category, Product, Service, Company, Banner, News, Swipers, Icons, Details,
                     Pictures, Link, Splitted, Footer])
