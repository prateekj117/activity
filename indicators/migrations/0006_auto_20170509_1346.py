# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-09 20:46
from __future__ import unicode_literals

from django.utils import timezone

from django.db import migrations
from django.db.models import Sum


def moveTargetedToPeriodicTargets(apps, schema_editor):
    CollectedData = apps.get_model("indicators", "CollectedData")
    PeriodicTarget = apps.get_model("indicators", "PeriodicTarget")
    Indicator = apps.get_model("indicators", "Indicator")
    """
    collecteddata = CollectedData.objects.all().order_by('indicator')
    counter = 1
    prev_indicator = 0
    for data in collecteddata:
        if prev_indicator != data.indicator.pk:
            prev_indicator = data.indicator.pk
            counter = 1
        pt = PeriodicTarget.objects.create(period="Temp %s" % counter,
                                      target=data.targeted,
                                      indicator=data.indicator,
                                      create_date=timezone.now())
        data.periodic_target = pt
        data.save()
        counter += 1
    """
    for ind in Indicator.objects.all():
        #sum_targets = ind.collecteddata_set.all().annotate(targets_sum=Sum('achieved'))[0].targets_sum
        targets_sum = ind.collecteddata_set.all().aggregate(
            total_sum=Sum('targeted'))['total_sum']
        if not targets_sum:
            targets_sum = 0
        pt = PeriodicTarget.objects.create(period="Temp label for periodic target",
                                           target=targets_sum,
                                           indicator=ind,
                                           create_date=timezone.now())
        ind.collecteddata_set.all().update(periodic_target=pt)


# https://github.com/toladata/TolaActivity/blob/new_dev/workflow/migrations/0013_auto_20170406_1012.py
class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0005_auto_20170509_1341'),
    ]

    operations = [
        migrations.RunPython(moveTargetedToPeriodicTargets),
    ]