from __future__ import unicode_literals

from django.db import models


class Call(models.Model):
    """
    This represents an API for generating a chart or report.
    """
    data = models.TextField()

