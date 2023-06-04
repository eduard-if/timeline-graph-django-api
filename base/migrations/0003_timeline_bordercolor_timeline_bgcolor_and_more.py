# Generated by Django 4.2.1 on 2023-06-04 08:17

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_item_title_alter_timeline_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeline',
            name='BorderColor',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='timeline',
            name='bgColor',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='timeline',
            name='textColor',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None),
        ),
    ]
