# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20160102_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote_content',
            name='vote_tit',
            field=models.CharField(max_length=32, blank=True),
            preserve_default=True,
        ),
    ]
