# Generated by Django 3.0.8 on 2020-07-27 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_k', '0003_remove_account_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_k',
            name='username',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
