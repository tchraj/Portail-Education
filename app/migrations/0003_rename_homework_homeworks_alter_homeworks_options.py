# Generated by Django 4.1.3 on 2023-02-09 21:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_alter_notes_options_homework'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Homework',
            new_name='Homeworks',
        ),
        migrations.AlterModelOptions(
            name='homeworks',
            options={'verbose_name': 'homeworks', 'verbose_name_plural': 'homeworks'},
        ),
    ]
