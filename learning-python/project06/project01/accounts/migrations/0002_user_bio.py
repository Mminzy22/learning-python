# Generated by Django 5.1.4 on 2025-01-15 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(default='Default Bio', max_length=255),
        ),
    ]
