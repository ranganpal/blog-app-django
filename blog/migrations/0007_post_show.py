# Generated by Django 5.0.4 on 2024-04-27 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='show',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
