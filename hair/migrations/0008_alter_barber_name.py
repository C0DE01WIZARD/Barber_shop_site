# Generated by Django 4.2.4 on 2023-09-03 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hair', '0007_alter_barber_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barber',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Ими барбера'),
        ),
    ]
