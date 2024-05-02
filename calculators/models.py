# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 18:19:32 2024

@author: conductor
"""

from django.db import models

class Calculator(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    URL = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class Solution(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField()
    URL = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.id}-{self.time}-{self.URL}"