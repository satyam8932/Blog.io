# Generated by Django 4.1.5 on 2023-01-05 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_posts_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='Date',
        ),
    ]
