# Generated by Django 3.2.9 on 2021-12-14 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_alter_material_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='lessons/materials', verbose_name='Materiais'),
        ),
    ]
