# Generated by Django 4.1.6 on 2023-06-27 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0015_rename_cosa_book_finished_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
    ]
