# Generated by Django 3.2.16 on 2023-09-07 20:26

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hair', '0014_alter_time_times'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField(max_length=25, verbose_name='Дата записи')),
            ],
        ),
        migrations.RemoveField(
            model_name='records',
            name='datetime',
        ),
        migrations.AddField(
            model_name='records',
            name='date',
            field=models.ForeignKey(null=True, on_delete=django.db.models.fields.CharField, to='hair.date'),
        ),
    ]
