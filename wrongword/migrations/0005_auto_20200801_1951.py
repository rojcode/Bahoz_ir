# Generated by Django 3.0.8 on 2020-08-01 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wrongword', '0004_auto_20200729_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wrong_word',
            name='dic',
        ),
        migrations.AlterField(
            model_name='wrong_word',
            name='answer',
            field=models.TextField(blank=True, default='بدون جواب', verbose_name='جواب ما'),
        ),
        migrations.AlterField(
            model_name='wrong_word',
            name='farsi',
            field=models.CharField(max_length=120, verbose_name='فارسی'),
        ),
        migrations.AlterField(
            model_name='wrong_word',
            name='kurdish',
            field=models.CharField(max_length=120, verbose_name='کردی'),
        ),
        migrations.AlterField(
            model_name='wrong_word',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='wrong_word',
            name='why_wrong',
            field=models.TextField(verbose_name='علت اشتباە بودی'),
        ),
    ]
