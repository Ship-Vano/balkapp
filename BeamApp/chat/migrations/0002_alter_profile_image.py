# Generated by Django 4.2.3 on 2023-07-23 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/default/user.png', upload_to='media/images'),
        ),
    ]