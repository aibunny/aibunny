# Generated by Django 4.1.3 on 2022-12-20 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0014_post_read_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='theblog.category',blank=True, null=True),
        ),
    ]