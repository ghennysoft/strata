# Generated by Django 4.2.7 on 2024-01-24 06:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('back', '0010_alter_emploi_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='souscrire',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]