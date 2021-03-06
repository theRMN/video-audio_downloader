# Generated by Django 3.2.8 on 2022-01-13 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_audio', '0009_videoinfo_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videoinfo',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='videoinfo',
            name='audio_url',
            field=models.URLField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='videoinfo',
            name='image',
            field=models.URLField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='videoinfo',
            name='video_url',
            field=models.URLField(max_length=1000),
        ),
    ]
