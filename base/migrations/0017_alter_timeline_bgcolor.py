# Generated by Django 4.2.1 on 2023-06-19 18:35

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_item_notesdetails_item_style'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='bgColor',
            field=colorfield.fields.ColorField(default='#30303034', image_field=None, max_length=18, samples=None),
        ),
    ]
