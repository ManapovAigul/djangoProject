# Generated by Django 4.0.3 on 2022-03-11 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('text', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
            ],
        ),
    ]
