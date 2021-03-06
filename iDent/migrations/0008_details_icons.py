# Generated by Django 4.0.3 on 2022-03-19 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iDent', '0007_swipers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(max_length=255, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Icons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
            ],
        ),
    ]
