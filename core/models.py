from django.db import models

# Create your models here.
class Marker(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    new = models.BooleanField()
    visits = models.IntegerField()

    def __repr__(self):
        return "[({0}, {1}) \tvisits: {2}]".format(self.x,self.y,self.visits)

    def color(self):
        return 'red'

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
