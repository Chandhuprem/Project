# Generated by Django 4.1.7 on 2023-03-09 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_newbook'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newbook',
            old_name='image',
            new_name='images',
        ),
    ]
