# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='candidade',
            field=models.ForeignKey(default=None, to='candidates.Candidate'),
            preserve_default=False,
        ),
    ]
