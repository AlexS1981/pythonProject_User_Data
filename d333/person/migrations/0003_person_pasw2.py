# Generated by Django 3.1.3 on 2020-11-30 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20201130_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='pasw2',
            field=models.CharField(default=123, max_length=20),
            preserve_default=False,
        ),
    ]
