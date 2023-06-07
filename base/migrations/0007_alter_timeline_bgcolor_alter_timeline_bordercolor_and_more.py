# Generated by Django 4.2.1 on 2023-06-04 13:35

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_timeline_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='bgColor',
            field=colorfield.fields.ColorField(default='#f8f9fa', image_field=None, max_length=18, samples=None),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='borderColor',
            field=colorfield.fields.ColorField(default='#adb5bd', image_field=None, max_length=18, samples=None),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='textColor',
            field=colorfield.fields.ColorField(default='#343a40', image_field=None, max_length=18, samples=None),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='titleColor',
            field=colorfield.fields.ColorField(default='#343a40', image_field=None, max_length=18, samples=None),
        ),
    ]
