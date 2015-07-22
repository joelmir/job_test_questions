# -*- coding: utf-8 -*-
from django.contrib import admin

from candidates.models import Candidate, Answer

admin.site.register(Candidate)
admin.site.register(Answer)