# Generated by Django 4.1.3 on 2022-12-19 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0013_alter_post_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='read_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]