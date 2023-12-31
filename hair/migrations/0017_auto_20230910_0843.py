# Generated by Django 3.2.16 on 2023-09-10 08:43

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hair', '0016_alter_records_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=250, verbose_name='Название')),
                ('number', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('address', models.TextField(max_length=100, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.AlterField(
            model_name='records',
            name='barbres',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hair.barber', verbose_name='Выберите барбера'),
        ),
        migrations.AlterField(
            model_name='records',
            name='date',
            field=models.ForeignKey(null=True, on_delete=django.db.models.fields.CharField, to='hair.date', verbose_name='Дата записи'),
        ),
        migrations.AlterField(
            model_name='records',
            name='time',
            field=models.ForeignKey(null=True, on_delete=django.db.models.fields.CharField, to='hair.time', verbose_name='Время записи'),
        ),
    ]
