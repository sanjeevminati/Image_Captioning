# Generated by Django 3.2.6 on 2021-08-03 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_remove_image_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/% Y/% m/% d/'),
        ),
    ]
