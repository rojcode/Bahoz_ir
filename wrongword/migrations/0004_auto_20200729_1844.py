# Generated by Django 3.0.8 on 2020-07-29 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrongword', '0003_wrong_word_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wrong_word',
            name='answer',
            field=models.TextField(blank=True, default='بدون جواب'),
        ),
    ]
