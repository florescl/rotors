# -*- coding: utf-8 -*-

import itertools
import random
import math
import matplotlib.pyplot as plt
import numpy as np
import random


from numpy import *
import mpl_toolkits.mplot3d.axes3d as p3
from random import randrange
from collections import defaultdict
from PIL import Image

iters = 20
dim = 200

n_iters_try_list = [20, 100, 150, 200, 250, 300, 350, 400, 450, 500]


def __MAIN__():


    w=100
    h=100
    l=100

    r=[[[4 for z in xrange (l)] for y in xrange(h)] for x in xrange(w)]
    p=[[[0 for z in xrange (l)] for y in xrange(h)] for x in xrange(w)] 
    g=[[[0 for z in xrange (l)] for y in xrange(h)] for x in xrange(w)] 
    u=0

    for k in xrange(100000):
        x=w//2
        y=h//2
        z=l//2
        while p[x][y][z]== 1:
            r[x][y][z]=(r[x][y][z]+1)%6
            u = r[x][y][z]
            (x,y,z)=[(x+1,y,z),(x,y+1,z),(x,y,z+1),(x-1,y,z),(x,y-1,z),(x,y,z-1)][r[x][y][z]]
        p[x][y][z]= 1
        g[x][y][z]= u 

    for z in xrange(l):
        im=Image.new('RGB',(500,500))
        pix=im.load()
        for x in xrange(w):
            for y in xrange(h):
                if p[x][y][z]== 1:
                    print g[x][y][z]
                    pix[x,y]=[(250,250,250),(255,0,0),(0,255,0),(0,0,255),(255,215,0),(128,0,0)][g[x][y][z]]
        im.save("imagexy_4_" + str(z) + ".gif") 
        #im.show()
        #im.close()


if __name__ == '__main__':
  __MAIN__()
