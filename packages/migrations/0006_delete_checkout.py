# Generated by Django 4.0.1 on 2022-04-12 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0005_checkout'),
    ]

    operations = [
        migrations.DeleteModel(
            name='checkout',
        ),
    ]