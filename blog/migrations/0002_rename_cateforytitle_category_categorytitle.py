# Generated by Django 4.1.5 on 2023-01-05 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cateforyTitle',
            new_name='categoryTitle',
        ),
    ]
