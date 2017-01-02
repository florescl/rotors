# -*- coding: utf-8 -*-

import itertools
import random
import math
import matplotlib.pyplot as plt
import numpy as np
import random

from random import randrange
from collections import defaultdict
from PIL import Image

iters = 20
dim = 200

k_list = [20, 100, 150, 200, 250, 300, 350, 400, 450, 500]


def __MAIN__():


    w=500
    h=500
    l=500
    r=[[0 for y in xrange(h)] for x in xrange(w)]
    p=[[0 for y in xrange(h)] for x in xrange(w)] 
    g=[[0 for y in xrange(h)] for x in xrange(w)] 
    u=0

    #for k in k_list:

    for k_ind in xrange(10000):
        x=w//2
        y=h//2
        while p[x][y]== 1:
            r[x][y]=(r[x][y]+1)%4
            u = r[x][y]
            (x,y)=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)][r[x][y]]
        p[x][y]= 1
        g[x][y]= u 

    im=Image.new('RGB',(500,500))
    pix=im.load()

    im2=Image.new('RGB',(500,500))
    pix2=im2.load()

    for x in xrange(w):
        for y in xrange(h):
            if p[x][y]== 1:
                pix[x,y]=[(250,250,250),(255,0,0),(0,255,0),(0,0,255)][g[x][y]]
                pix2[x,y] = [(250,250,250),(255,0,0),(0,255,0),(0,0,255)][r[x][y]]
    im2.save("rotors2d_0_" + str(10000) + ".gif")
    im.save("image2d_0_" + str(10000) + ".gif") 


if __name__ == '__main__':
  __MAIN__()
