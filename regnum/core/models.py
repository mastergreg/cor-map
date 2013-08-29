from django.db import models

# Create your models here.
class Markers(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()

    def __unicode__(self):
        return self.address
