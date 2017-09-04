# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_auto_20160627_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='instancetest',
            name='url_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'HTTPS'), (1, 'Tor')], default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='instancetest',
            name='certificate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stats.Certificate'),
        ),
        migrations.AlterField(
            model_name='instancetest',
            name='url',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stats.Url'),
        ),
        migrations.AlterUniqueTogether(
            name='instancetest',
            unique_together=set([('timestamp', 'instance', 'url_type')]),
        ),
        migrations.AlterUniqueTogether(
            name='url',
            unique_together=set([('url',)]),
        ),
    ]