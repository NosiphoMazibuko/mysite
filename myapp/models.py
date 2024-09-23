from django.db import models

class BandMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

