# Generated by Django 2.1 on 2018-09-12 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expert', '0011_auto_20180912_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paperinfo',
            name='author2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paperinfo',
            name='author3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paperinfo',
            name='author4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paperinfo',
            name='author5',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
