# Generated by Django 2.1.5 on 2019-02-14 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthCentre', '0007_auto_20190213_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='new',
            field=models.BooleanField(default=True),
        ),
    ]
