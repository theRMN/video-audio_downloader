# Generated by Django 3.2.8 on 2021-12-20 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_audio', '0006_auto_20211220_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videoinfo',
            old_name='audio',
            new_name='audio_url',
        ),
        migrations.RenameField(
            model_name='videoinfo',
            old_name='url',
            new_name='video_url',
        ),
    ]
