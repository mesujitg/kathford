# Generated by Django 4.0.5 on 2023-03-07 05:41

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'verbose_name': '2. Content'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': '1. Section'},
        ),
        migrations.AlterField(
            model_name='content',
            name='details',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
