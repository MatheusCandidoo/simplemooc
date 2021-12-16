# Generated by Django 3.2.9 on 2021-12-12 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20211212_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcements',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='courses.course', verbose_name='Curso'),
        ),
    ]