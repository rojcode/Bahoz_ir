# Generated by Django 3.0.8 on 2020-07-27 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_k', '0002_auto_20200727_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account_k',
            name='id',
        ),
    ]
