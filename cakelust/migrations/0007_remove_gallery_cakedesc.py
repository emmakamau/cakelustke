# Generated by Django 3.2.6 on 2021-08-15 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cakelust', '0006_auto_20210815_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='cakedesc',
        ),
    ]
