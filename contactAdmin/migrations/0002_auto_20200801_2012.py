# Generated by Django 3.0.8 on 2020-08-01 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactAdmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactadminmodel',
            options={'verbose_name': 'ارتباط با مدیر', 'verbose_name_plural': 'ارتباط با مدیران'},
        ),
        migrations.AlterField(
            model_name='contactadminmodel',
            name='message',
            field=models.CharField(max_length=120, verbose_name='پیغام'),
        ),
        migrations.AlterField(
            model_name='contactadminmodel',
            name='subject',
            field=models.CharField(max_length=120, verbose_name='موضوع'),
        ),
        migrations.AlterField(
            model_name='contactadminmodel',
            name='user',
            field=models.CharField(max_length=120, verbose_name='کاربر'),
        ),
    ]
