# Generated by Django 4.0.4 on 2022-04-29 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_profile_agree_remove_profile_sex_profile_img2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='img2',
        ),
        migrations.AddField(
            model_name='profile',
            name='agree',
            field=models.BooleanField(default=False, verbose_name='Згода'),
        ),
        migrations.AddField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('meal', 'Чоловік'), ('femeal', 'Жінка')], default=None, max_length=100, verbose_name='Стать'),
        ),
    ]
