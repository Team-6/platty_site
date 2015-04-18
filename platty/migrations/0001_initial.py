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
            name='Contribution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.DecimalField(max_digits=11, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('date_time', models.DateTimeField()),
                ('name', models.CharField(max_length=64)),
                ('addressLineOne', models.CharField(max_length=128)),
                ('addressLineTwo', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=36)),
                ('state', models.CharField(max_length=2)),
                ('zipCode', models.PositiveIntegerField(max_length=5)),
                ('description', models.CharField(max_length=1024)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('description', models.CharField(max_length=256)),
                ('quanitity', models.IntegerField(max_length=11)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('event', models.ForeignKey(to='platty.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.IntegerField(default=1, max_length=1, choices=[(0, b'Owner'), (1, b'Goer')])),
                ('event', models.ForeignKey(to='platty.Event')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='donation',
            name='event',
            field=models.ForeignKey(to='platty.Event'),
        ),
        migrations.AddField(
            model_name='donation',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contribution',
            name='event',
            field=models.ForeignKey(to='platty.Event'),
        ),
        migrations.AddField(
            model_name='contribution',
            name='requirement',
            field=models.ForeignKey(to='platty.Requirement'),
        ),
        migrations.AddField(
            model_name='contribution',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
