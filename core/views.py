from django.shortcuts import render_to_response
from django.template import RequestContext
import Image, ImageDraw
from .models import Marker

WORLD_WIDTH=6144
WORLD_HEIGHT=6144

IMAGE_WIDTH=10000
IMAGE_HEIGHT=10000


SQSIZE=3
LQSIZE=2

def landing(request):
    '''
    im = Image.open("map.png")
    global IMAGE_WIDTH
    global IMAGE_HEIGHT
    IMAGE_WIDTH, IMAGE_HEIGHT = im.size
    draw = ImageDraw.Draw(im)
    net = Marker.objects.all()
    print net.values()
    for row in net.values():
        for pt in row.values():
            print pt
            color = pt.color()
            x,y = normalize(pt.getX(), pt.getY())
            draw.ellipse((x-SQSIZE, y-SQSIZE, x+SQSIZE, y+SQSIZE), outline='white')
            draw.point((x, y), fill='yellow')
            draw.ellipse((x-LQSIZE, y-LQSIZE, x+LQSIZE, y+LQSIZE), fill=color)
    im.save("map.png", "PNG")
    '''

    return render_to_response("landing.html", locals(), RequestContext(request))

def normalize(x,y):
    return (IMAGE_WIDTH*x/WORLD_WIDTH, IMAGE_HEIGHT*y/WORLD_HEIGHT)
