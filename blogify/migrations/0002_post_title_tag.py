# Generated by Django 4.0.6 on 2022-09-05 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Blogify Today', max_length=255),
        ),
    ]
