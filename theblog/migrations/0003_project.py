# Generated by Django 4.1.6 on 2023-03-05 20:39

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0002_alter_post_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', ckeditor_uploader.fields.RichTextUploadingField()),
                ('tittle', ckeditor_uploader.fields.RichTextUploadingField()),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date', models.DateField(auto_now_add=True)),
                ('git_url', models.URLField()),
                ('web_url', models.URLField(blank=True)),
                ('kaggle_url', models.URLField(blank=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='theblog.category')),
            ],
        ),
    ]
