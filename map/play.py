#!/usr/bin/env python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : play.py
# Creation Date : 29-08-2013
# Last Modified : Thu 29 Aug 2013 02:30:14 AM EEST
# Created By : Greg Liras <gregliras@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/

import Image, ImageDraw

WORLD_WIDTH=10000
WORLD_HEIGHT=10000

IMAGE_WIDTH=10000
IMAGE_HEIGHT=10000

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visits = 1

    def color(self):
        pass

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def visit(self):
        self.visits += 1


class Network(object):
    def __init__(self):
        self.points = {}

    def add(self, point):
        x = point.getX()
        y = point.getY()

        try:
            row = self.points[x]
            try:
                p = row[y]
                p.visit()
            except KeyError:
                row[y] = point
        except KeyError:
            self.points[x] = {y : point}
    def values(self):
        return self.points.values()


def read_net(f = "points.dat"):
    net = Network()
    fp = open(f)
    for line in fp:
        x,y = map(int, line.split())
        net.add(Point(x,y))
    fp.close()
    return net


def normalize(x,y):
    return (IMAGE_WIDTH*x/WORLD_WIDTH, IMAGE_HEIGHT*y/WORLD_HEIGHT)
    
def main():
    im = Image.open("map.png")
    global IMAGE_WIDTH
    global IMAGE_HEIGHT
    IMAGE_WIDTH, IMAGE_HEIGHT = im.size
    draw = ImageDraw.Draw(im)
    net = read_net()
    print net.values()
    for row in net.values():
        print row
        for pt in row.values():
            x,y = normalize(pt.getX(), pt.getY())
            draw.rectangle([x+2, y+2, x-2, y-2])
    im.show()


if __name__=="__main__":
    main()


