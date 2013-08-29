from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
import Image, ImageDraw
from .models import Marker

WORLD_WIDTH=6144
WORLD_HEIGHT=6144

IMAGE_WIDTH=10000
IMAGE_HEIGHT=10000

SQSIZE=3
LQSIZE=2

@login_required
def landing(request):
    im = Image.open("media/trans_map.png")
    global IMAGE_WIDTH
    global IMAGE_HEIGHT
    IMAGE_WIDTH, IMAGE_HEIGHT = im.size
    draw = ImageDraw.Draw(im)
    markers = Marker.objects.all()
    for pt in markers:
            # print pt
            x,y = normalize(pt.getX(), pt.getY())
            draw.rectangle([x+2, y+2, x-2, y-2])
    im.save("media/trans_map.png", "PNG")

    return render_to_response("landing.html", locals(), RequestContext(request))

def normalize(x,y):
    return (IMAGE_WIDTH*x/WORLD_WIDTH, IMAGE_HEIGHT*y/WORLD_HEIGHT)
