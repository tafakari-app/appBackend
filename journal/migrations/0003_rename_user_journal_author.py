# Generated by Django 4.2.3 on 2023-07-30 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_rename_author_journal_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journal',
            old_name='user',
            new_name='author',
        ),
    ]
