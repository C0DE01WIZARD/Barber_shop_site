# Generated by Django 3.2.16 on 2023-09-09 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hair', '0015_auto_20230907_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='name',
            field=models.CharField(default='', max_length=24, verbose_name='Ваше имя'),
        ),
    ]