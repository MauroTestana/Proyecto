# Generated by Django 4.0.3 on 2022-04-10 20:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiantes',
            name='apellido',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
