# Generated by Django 3.2.8 on 2021-12-30 04:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video_audio', '0008_videoinfo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoinfo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
