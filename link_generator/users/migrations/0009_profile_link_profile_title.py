# Generated by Django 4.0.4 on 2022-05-09 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='link',
            field=models.SlugField(default='url'),
        ),
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.CharField(default='name', max_length=250),
        ),
    ]
