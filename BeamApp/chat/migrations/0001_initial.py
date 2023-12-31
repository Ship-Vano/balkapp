# Generated by Django 4.2.3 on 2023-07-22 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(default='Новое обсуждение', max_length=100)),
                ('post_content', models.CharField(max_length=5000)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(default='', upload_to='images')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Replie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_content', models.CharField(max_length=5000)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(default='', upload_to='images')),
                ('post', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='chat.post')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='BeamApp/media/default/user.png', upload_to='BeamApp/media/images')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=300)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('link', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_updated'],
                'indexes': [models.Index(fields=['-date_updated'], name='chat_forum_date_up_d04da8_idx')],
            },
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discuss', models.CharField(max_length=1000)),
                ('forum', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='chat.forum')),
                ('participants', models.ManyToManyField(blank=True, related_name='rooms_joined', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
