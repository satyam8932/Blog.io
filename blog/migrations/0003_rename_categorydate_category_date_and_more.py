# Generated by Django 4.1.5 on 2023-01-05 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_cateforytitle_category_categorytitle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='categoryDate',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='categoryDescription',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='categoryID',
            new_name='ID',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='categoryImage',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='categoryTitle',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='categoryUrl',
            new_name='Url',
        ),
        migrations.RenameField(
            model_name='posts',
            old_name='postCategory',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='posts',
            old_name='postContent',
            new_name='Content',
        ),
        migrations.RenameField(
            model_name='posts',
            old_name='postId',
            new_name='Id',
        ),
        migrations.RenameField(
            model_name='posts',
            old_name='postImage',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='posts',
            old_name='postTitle',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='posts',
            old_name='postUrl',
            new_name='Url',
        ),
    ]
