# Generated by Django 3.2.9 on 2021-12-12 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_comments_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcements',
            old_name='title',
            new_name='tittle',
        ),
    ]
