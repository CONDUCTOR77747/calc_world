"""
Model for storing solution history list in database
"""
from django.db import models
from django.db.models.manager import Manager


class Solution(models.Model):
    """ Represents a solution entity """
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField()
    URL = models.URLField(max_length=200)
    objects: Manager['Solution'] = models.Manager()

    def __str__(self) -> str:
        """
        Returns
        -------
        str
            String representation of the Solution instance.

        """
        return f"{self.id}-{self.time}-{self.URL}"
