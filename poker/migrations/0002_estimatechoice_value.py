# Generated by Django 3.2.3 on 2022-07-10 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estimatechoice',
            name='value',
            field=models.IntegerField(default=0),
        ),
    ]
