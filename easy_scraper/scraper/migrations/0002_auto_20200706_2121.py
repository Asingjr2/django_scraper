# Generated by Django 3.0.8 on 2020-07-07 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='name',
            new_name='link_name',
        ),
    ]
