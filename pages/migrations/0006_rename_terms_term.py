# Generated by Django 4.0.1 on 2022-04-18 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_terms'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='terms',
            new_name='term',
        ),
    ]