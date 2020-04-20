# Generated by Django 2.2.10 on 2020-04-09 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0021_merge_20200409_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fundcode',
            name='funding',
        ),
        migrations.AddField(
            model_name='fundcode',
            name='percentage_of_funding',
            field=models.IntegerField(blank=True, default=5, verbose_name='% of Funding'),
            preserve_default=False,
        ),
    ]