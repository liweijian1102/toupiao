# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote_content',
            name='content_zuozhe',
            field=models.CharField(max_length=32, blank=True),
            preserve_default=True,
        ),
    ]
