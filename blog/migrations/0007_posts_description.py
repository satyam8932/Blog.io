# Generated by Django 4.1.5 on 2023-01-05 08:03

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_posts_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='Description',
            field=models.TextField(default=builtins.print),
            preserve_default=False,
        ),
    ]
