from django.db import models


ERROR_MARGIN = 50

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
            SYRTIS: "#00FF00",
            ALSIUS: "#0000FF",
            IGNIS: "#FF0000"
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
        super(Marker, self).save()

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def visit(self, other):
        self.new = True
        self.x = int(round((self.x*self.visits + other.x*other.visits)/float(self.visits+other.visits)))
        self.y = int(round((self.y*self.visits + other.y*other.visits)/float(self.visits+other.visits)))
        self.visits += other.visits

    def __unicode__(self):
        return str(self.x) + " " + str(self.y)

    def save(self, *args, **kwargs):
        markers = Marker.objects.filter(realm = self.realm, 
                x__range = (self.x - ERROR_MARGIN, self.x + ERROR_MARGIN),
                y__range = (self.y - ERROR_MARGIN, self.y + ERROR_MARGIN))
        if markers.exists():
            for pt in markers:
                if pt.pk != self.pk:
                    pt.visit(self)
                    super(Marker, pt).save(*args, **kwargs) # Call the "real" save() method.
        else:
            super(Marker, self).save(*args, **kwargs) # Call the "real" save() method.
