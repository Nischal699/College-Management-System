# Generated by Django 4.2.11 on 2025-03-20 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='blog_icon',
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(default=None, upload_to='blog_images/'),
        ),
    ]
