# Generated by Django 5.0.4 on 2024-04-26 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='status',
            new_name='active',
        ),
    ]
