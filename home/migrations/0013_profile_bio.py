# Generated by Django 3.1.4 on 2021-03-23 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20210323_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]