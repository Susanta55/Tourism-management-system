# Generated by Django 4.0.1 on 2022-02-19 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0007_alter_package_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]
