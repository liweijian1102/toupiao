# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote_title', models.CharField(max_length=32)),
                ('vote_start', models.DateTimeField()),
                ('vote_end', models.DateTimeField()),
                ('vote_zuozhe', models.CharField(max_length=32, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='vote_content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote_bt', models.CharField(max_length=32)),
                ('vote_a', models.CharField(max_length=32, blank=True)),
                ('vote_b', models.CharField(max_length=32, blank=True)),
                ('vote_c', models.CharField(max_length=32, blank=True)),
                ('vote_d', models.CharField(max_length=32, blank=True)),
                ('vote_e', models.CharField(max_length=32, blank=True)),
                ('vote_f', models.CharField(max_length=32, blank=True)),
                ('vote_type', models.CharField(max_length=32, blank=True)),
                ('content_zuozhe', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='vote_ip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('voteip', models.IPAddressField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='vote_result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result_bt', models.CharField(max_length=32)),
                ('result_aa', models.IntegerField(max_length=10, blank=True)),
                ('result_bb', models.IntegerField(max_length=10, blank=True)),
                ('result_cc', models.IntegerField(max_length=10, blank=True)),
                ('result_dd', models.IntegerField(max_length=10, blank=True)),
                ('result_ee', models.IntegerField(max_length=10, blank=True)),
                ('result_ff', models.IntegerField(max_length=10, blank=True)),
                ('content_zuozhe', models.CharField(max_length=32, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
