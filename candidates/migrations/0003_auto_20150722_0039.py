# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_answer_candidade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='candidade',
            new_name='candidate',
        ),
    ]
