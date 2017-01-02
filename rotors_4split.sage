w=500
h=500
r=[[0 for y in xrange(h)] for x in xrange(w)]
p=[[0 for y in xrange(h)] for x in xrange(w)] 
g=[[0 for y in xrange(h)] for x in xrange(w)] 
u=0
for k in xrange(10000):
    x=w//2
    y=h//2
    while p[x][y]== 1:
        r[x][y]=(r[x][y]+1)%4
        u = r[x][y]
        (x,y)=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)][r[x][y]]
    p[x][y]= 1
    g[x][y]= u 
   
from PIL import Image
im=Image.new('RGB',(500,500))
pix=im.load()

for x in xrange(w):
    for y in xrange(h):
        if p[x][y]== 1:
         pix[x,y]=[(250,250,250),(255,0,0),(0,255,0),(0,0,255)][g[x][y]]
im.save("a.gif") 