# Generated by Django 4.1.2 on 2022-11-10 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Recruiter', 'recruiter'), ('Candidate', 'candidate')], default='recruiter', max_length=9),
        ),
    ]