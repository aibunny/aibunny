# Generated by Django 4.1.3 on 2022-12-19 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0012_alter_post_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]