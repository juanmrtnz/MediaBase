# Generated by Django 4.1.6 on 2023-06-27 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0017_book_cosa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='finished_date',
            new_name='language',
        ),
    ]
