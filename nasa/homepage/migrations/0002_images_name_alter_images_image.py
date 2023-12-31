# Generated by Django 4.1 on 2023-06-23 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='name',
            field=models.CharField(default=1, max_length=255, verbose_name='Название изображения'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]
