# Generated by Django 4.2.5 on 2023-10-02 07:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body2',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
