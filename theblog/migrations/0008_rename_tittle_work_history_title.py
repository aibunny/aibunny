# Generated by Django 4.1.6 on 2023-05-24 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0007_remove_work_history_end_work_history_end'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work_history',
            old_name='tittle',
            new_name='title',
        ),
    ]