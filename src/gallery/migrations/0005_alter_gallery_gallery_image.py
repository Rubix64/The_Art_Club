# Generated by Django 3.2.9 on 2021-12-16 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_alter_gallery_gallery_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='gallery_image',
            field=models.ImageField(upload_to='gallery/images'),
        ),
    ]
