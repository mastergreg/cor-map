from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
import Image, ImageDraw
from .models import Marker

import deepzoom

WORLD_WIDTH=6144
WORLD_HEIGHT=6144

IMAGE_WIDTH=10000
IMAGE_HEIGHT=10000

SQSIZE=3
LQSIZE=2

def save_data(markers, f = "media/points.dat"):
    fp = open(f, 'w')
    for m in markers:
        fp.write("{0} {1}\n".format(m.getX(), m.getY()))
    fp.close()


def fix_data(f = "media/points.dat"):
    fp = open(f)
    for line in fp:
        x,y = map(int, line.split())
        m = Marker()
        m.x = x
        m.y = y
        m.new = True
        m.visits = 1
        m.save()
    fp.close()

@login_required
def landing(request):
    #fix_data()
    global IMAGE_WIDTH
    global IMAGE_HEIGHT
    markers = Marker.objects.filter(new = True)
    #save_data(markers)
    print len(markers)
    if len(markers) > 0:
        im = Image.open("media/map_full.png")
        IMAGE_WIDTH, IMAGE_HEIGHT = im.size
        draw = ImageDraw.Draw(im)

        for pt in markers:
                #print pt
                pt.check()
                pt.save()
                x,y = normalize(pt.getX(), pt.getY())
                draw.rectangle([(x-SQSIZE, y-SQSIZE), (x+SQSIZE, y+SQSIZE)], fill="white")

        im.save("media/map_full.png", "PNG")
        dz_creator = deepzoom.ImageCreator(tile_size=128, tile_overlap=2, tile_format="png",
                                                image_quality=0.8, resize_filter="bicubic")
        dz_creator.create("media/map_full.png", "media/map_full.xml")


    return render_to_response("landing.html", locals(), RequestContext(request))

def normalize(x,y):
    return (IMAGE_WIDTH*x/WORLD_WIDTH, IMAGE_HEIGHT*y/WORLD_HEIGHT)
