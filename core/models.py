from django.db import models

# Create your models here.
class Marker(models.Model):
    SYRTIS = "S"
    ALSIUS = "A"
    IGNIS = "I"
    REALM_CHOICES = (
            (SYRTIS, "Syrtis"),
            (ALSIUS, "Alsius"),
            (IGNIS, "Ignis")
            )
    COLOR_CHOICES = {
            SYRTIS: "#00CC00",
            ALSIUS: "#336699",
            IGNIS: "#DC143C"
            }

    x = models.IntegerField()
    y = models.IntegerField()
    new = models.BooleanField(default = True)
    visits = models.IntegerField(default = 1)
    realm = models.CharField(max_length = 1, choices = REALM_CHOICES, default = SYRTIS)

    def __repr__(self):
        return "[({0}, {1}) \tvisits: {2}]".format(self.x,self.y,self.visits)

    def color(self):
        return self.COLOR_CHOICES[self.realm]

    def check(self):
        self.new = False

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def visit(self):
        self.visits += 1

    def __unicode__(self):
        return str(self.x) + " " + str(self.y)

    def save(self, *args, **kwargs):
        markers = Marker.objects.filter(realm = self.realm, 
                x__range = (self.x - 5, self.x + 5),
                y__range = (self.y - 5, self.y + 5))
        if markers.exists():
            for pt in markers:
                pt.visit()
                return
        else:
            super(Marker, self).save(*args, **kwargs) # Call the "real" save() method.
