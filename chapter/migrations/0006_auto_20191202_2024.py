# Generated by Django 2.2.7 on 2019-12-03 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chapter', '0005_chapteruser_has_been_authenticated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumni',
            old_name='member',
            new_name='user',
        ),
    ]
