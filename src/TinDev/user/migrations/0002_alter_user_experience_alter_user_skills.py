# Generated by Django 4.1.2 on 2022-11-09 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='experience',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='skills',
            field=models.TextField(null=True),
        ),
    ]