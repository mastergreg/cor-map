from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
import Image, ImageDraw
from .models import Marker

WORLD_WIDTH=6144
WORLD_HEIGHT=6144

IMAGE_WIDTH=10000
IMAGE_HEIGHT=10000

SQSIZE=4
LQSIZE=3

def fix_data(f = "media/points.dat"):
    fp = open(f)
    for line in fp:
        x,y = map(int, line.split())
        m = Marker()
        m.x = x
        m.y = y
        m.save()
    fp.close()

@login_required
def landing(request):
    #fix_data()
    im = Image.open("media/trans_empty.png")
    global IMAGE_WIDTH
    global IMAGE_HEIGHT
    IMAGE_WIDTH, IMAGE_HEIGHT = im.size
    draw = ImageDraw.Draw(im)
    markers = Marker.objects.all()
    for pt in markers:
            print pt
            x,y = normalize(pt.getX(), pt.getY())
            draw.rectangle([(x-SQSIZE, y-SQSIZE), (x+SQSIZE, y+SQSIZE)], fill=(255, 255))
    im.save("media/trans_map.png", "PNG")

    return render_to_response("landing.html", locals(), RequestContext(request))

def normalize(x,y):
    return (IMAGE_WIDTH*x/WORLD_WIDTH, IMAGE_HEIGHT*y/WORLD_HEIGHT)
