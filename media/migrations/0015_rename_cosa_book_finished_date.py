# Generated by Django 4.1.6 on 2023-06-27 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0014_remove_book_finished_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='cosa',
            new_name='finished_date',
        ),
    ]