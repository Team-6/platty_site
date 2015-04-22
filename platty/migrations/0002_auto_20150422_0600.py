# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('platty', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requirement',
            old_name='quanitity',
            new_name='quantity',
        ),
    ]
