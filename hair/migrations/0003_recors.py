# Generated by Django 4.2.3 on 2023-07-31 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hair', '0002_auto_20230722_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='Время и дата записи')),
                ('barbres', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hair.barber')),
            ],
        ),
    ]
