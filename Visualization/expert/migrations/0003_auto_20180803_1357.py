# Generated by Django 2.0.3 on 2018-08-03 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expert', '0002_auto_20180803_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paperinfo',
            name='author1',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
    ]
