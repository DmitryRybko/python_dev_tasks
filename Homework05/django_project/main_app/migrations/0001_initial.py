# Generated by Django 3.2.7 on 2021-09-04 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('add_date', models.DateTimeField(verbose_name='Дата поступления')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('units', models.CharField(max_length=255, verbose_name='Ед. измеренеия')),
                ('supplier_name', models.CharField(max_length=255, verbose_name='Имя поставщика')),
            ],
        ),
    ]
