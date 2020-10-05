# Generated by Django 3.0.8 on 2020-07-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurdishdic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kurdishdic',
            name='dic',
        ),
        migrations.AddField(
            model_name='kurdishdic',
            name='kurmanci',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='kurdishdic',
            name='sorani',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='kurdishdic',
            name='word_id',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
