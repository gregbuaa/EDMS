# Generated by Django 2.0.3 on 2018-08-03 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expert', '0003_auto_20180803_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paperinfo',
            name='author2',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paperinfo',
            name='author3',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paperinfo',
            name='author4',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paperinfo',
            name='author5',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
    ]
