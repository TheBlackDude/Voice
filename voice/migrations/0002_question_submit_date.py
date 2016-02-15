# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('voice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='submit_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2016, 1, 28)),
            preserve_default=False,
        ),
    ]
