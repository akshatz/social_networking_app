# Generated by Django 2.2.6 on 2019-11-09 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191109_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='profile_pics'),
        ),
    ]
