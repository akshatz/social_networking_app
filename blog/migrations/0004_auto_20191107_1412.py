# Generated by Django 2.2.6 on 2019-11-07 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191107_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='video',
            field=models.FileField(null=True, upload_to='', verbose_name='Video'),
        ),
    ]