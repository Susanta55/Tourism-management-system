# Generated by Django 4.0.1 on 2022-02-19 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0002_alter_package_is_featured_alter_package_transport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]