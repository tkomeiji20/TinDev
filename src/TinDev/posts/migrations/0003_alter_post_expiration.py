# Generated by Django 4.1.2 on 2022-11-28 01:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 31, 0, 0)),
        ),
    ]
