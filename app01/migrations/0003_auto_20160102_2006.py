# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20160101_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='vote_end',
            field=models.DateField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vote',
            name='vote_start',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
