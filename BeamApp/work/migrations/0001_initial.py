# Generated by Django 4.2.1 on 2023-07-07 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('var1', models.FloatField(default=0)),
                ('var2', models.FloatField(default=0)),
                ('var3', models.FloatField(default=0)),
                ('var4', models.FloatField(default=0)),
                ('var5', models.FloatField(default=0)),
                ('var6', models.FloatField(default=0)),
                ('var7', models.FloatField(default=0)),
                ('var8', models.FloatField(default=0)),
                ('var9', models.FloatField(default=0)),
                ('var10', models.FloatField(default=0)),
                ('var11', models.FloatField(default=0)),
                ('var12', models.FloatField(default=0)),
                ('rez1', models.FloatField(default=0)),
                ('rez2', models.FloatField(default=0)),
            ],
        ),
    ]
