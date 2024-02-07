# Generated by Django 4.2.7 on 2023-11-30 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile',
            field=models.CharField(choices=[('Consommateur', 'Consommateur'), ('Ambassadeur', 'Ambassadeur'), ('Partenaire', 'Partenaire')], max_length=15, verbose_name='profile'),
        ),
    ]