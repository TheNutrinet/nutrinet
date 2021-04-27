# Generated by Django 3.1.7 on 2021-04-11 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=users.models.upload_location)),
                ('occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('nationality', models.CharField(blank=True, max_length=255, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('poids', models.PositiveIntegerField(blank=True, default='1', null=True)),
                ('taille', models.PositiveIntegerField(blank=True, default='1', null=True)),
                ('date_de_naissance', models.DateField(blank=True, null=True)),
                ('genre', models.CharField(blank=True, default='Femme', max_length=200, null=True)),
                ('activite', models.CharField(blank=True, default='None', max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
