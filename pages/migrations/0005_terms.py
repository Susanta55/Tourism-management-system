# Generated by Django 4.0.1 on 2022-04-18 14:53

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_about_about_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='terms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms_text', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
