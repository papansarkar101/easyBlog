# Generated by Django 3.1.3 on 2020-11-21 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201121_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='Gibberish', max_length=255),
        ),
    ]
