# Generated by Django 4.1.2 on 2022-12-06 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_experience'),
        ('posts', '0005_post_interest'),
        ('offers', '0002_alter_offers_post_alter_offers_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='post',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
        ),
        migrations.AlterField(
            model_name='offers',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]