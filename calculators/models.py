from django.db import models

class Solution(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField()
    URL = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.id}-{self.time}-{self.URL}"