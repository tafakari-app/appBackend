# Generated by Django 4.2.3 on 2023-08-10 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0008_remove_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='emotion_predications',
        ),
        migrations.RemoveField(
            model_name='post',
            name='emotions',
        ),
    ]
