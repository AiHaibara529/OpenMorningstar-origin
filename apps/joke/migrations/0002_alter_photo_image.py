# Generated by Django 4.0.4 on 2022-05-17 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joke', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, upload_to='photo/%Y%m%d%H%M%S/', verbose_name='本站托管图片'),
        ),
    ]
