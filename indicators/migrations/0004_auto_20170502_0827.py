# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-02 15:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0003_disaggregationlabel_customsort'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataCollectionFrequency',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.CharField(
                    blank=True, max_length=135, null=True)),
                ('description', models.CharField(
                    blank=True, max_length=255, null=True)),
                ('numdays', models.PositiveIntegerField(
                    default=0, verbose_name=b'Frequency in number of days')),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='historicalindicator',
            name='data_issues',
            field=models.TextField(
                blank=True, max_length=500, null=True, verbose_name=b'Data Issues'),
        ),
        migrations.AddField(
            model_name='historicalindicator',
            name='data_points',
            field=models.TextField(
                blank=True, max_length=500, null=True, verbose_name=b'Data Points'),
        ),
        migrations.AddField(
            model_name='historicalindicator',
            name='indicator_changes',
            field=models.TextField(
                blank=True, max_length=500, null=True, verbose_name=b'Changes to Indicator'),
        ),
        migrations.AddField(
            model_name='historicalindicator',
            name='justification',
            field=models.TextField(blank=True, max_length=500, null=True,
                                   verbose_name=b'Rationale or Justification for Indicator'),
        ),
        migrations.AddField(
            model_name='historicalindicator',
            name='quality_assurance',
            field=models.TextField(
                blank=True, max_length=500, null=True, verbose_name=b'Quality Assurance Measures'),
        ),
        migrations.AddField(
            model_name='historicalindicator',
            name='rationale_for_target',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='historicalindicator',
            name='unit_of_measure',
            field=models.CharField(
                blank=True, max_length=135, null=True, verbose_name=b'Unit of Measure'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='data_issues',
            field=models.TextField(
                blank=True, max_length=500, null=True, verbose_name=b'Data Issues'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='data_points',
            field=models.TextField(
                blank=True, max_length=500, null=True, verbose_name=b'Data Points'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='indicator_changes',
            field=models.TextField(
                blank=True, max_length=500, null=True, verbose_name=b'Changes to Indicator'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='justification',
            field=models.TextField(blank=True, max_length=500, null=True,
                                   verbose_name=b'Rationale or Justification for Indicator'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='quality_assurance',
            field=models.TextField(
                blank=True, max_length=500, null=True, verbose_name=b'Quality Assurance Measures'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='rationale_for_target',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='indicator',
            name='unit_of_measure',
            field=models.CharField(
                blank=True, max_length=135, null=True, verbose_name=b'Unit of Measure'),
        ),
        migrations.AlterField(
            model_name='historicalindicator',
            name='data_collection_method',
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name=b'Data Collection Method'),
        ),
        migrations.AlterField(
            model_name='historicalindicator',
            name='information_use',
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name=b'Information User'),
        ),
        migrations.AlterField(
            model_name='historicalindicator',
            name='means_of_verification',
            field=models.CharField(blank=True, max_length=255, null=True,
                                   verbose_name=b'Means of Verification / Data Source'),
        ),
        migrations.AlterField(
            model_name='historicalindicator',
            name='method_of_analysis',
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name=b'Method of Analysis'),
        ),
        migrations.AlterField(
            model_name='historicalindicator',
            name='responsible_person',
            field=models.CharField(blank=True, max_length=255, null=True,
                                   verbose_name=b'Responsible Person(s) and Team'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='data_collection_method',
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name=b'Data Collection Method'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='information_use',
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name=b'Information User'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='means_of_verification',
            field=models.CharField(blank=True, max_length=255, null=True,
                                   verbose_name=b'Means of Verification / Data Source'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='method_of_analysis',
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name=b'Method of Analysis'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='reporting_frequency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='indicators.ReportingFrequency', verbose_name=b'Frequency of Reporting'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='responsible_person',
            field=models.CharField(blank=True, max_length=255, null=True,
                                   verbose_name=b'Responsible Person(s) and Team'),
        ),
        migrations.AddField(
            model_name='historicalindicator',
            name='data_collection_frequency',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True,
                                    on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='indicators.DataCollectionFrequency'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='data_collection_frequency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='indicators.DataCollectionFrequency', verbose_name=b'Frequency of Data Collection'),
        ),
    ]