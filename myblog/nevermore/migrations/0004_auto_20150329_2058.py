# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nevermore', '0003_auto_20150329_2057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='published',
            new_name='publish',
        ),
    ]
