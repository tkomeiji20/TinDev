# Generated by Django 4.1.2 on 2022-11-09 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('Part-Time', 'part'), ('Full-Time', 'full')], max_length=10)),
                ('location', models.CharField(max_length=50)),
                ('skills', models.TextField()),
                ('description', models.TextField()),
                ('company', models.CharField(max_length=20)),
                ('expiration', models.DateTimeField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
