# Generated by Django 2.0.7 on 2018-07-12 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20180712_1442'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-id']},
        ),
    ]
