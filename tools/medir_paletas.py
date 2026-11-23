import sys, numpy as np, colorsys
from PIL import Image
hx=lambda c:'#%02x%02x%02x'%tuple(int(round(v)) for v in c)
def load(p): return np.asarray(Image.open(p).convert('RGB')).astype(float)
def reg(a,n,x0,y0,x1,y1):
    r=a[y0:y1,x0:x1].reshape(-1,3); print(f'  {n:14s} med {hx(np.median(r,0))} mean {hx(r.mean(0))}')
bw=load(sys.argv[1])
print('DIA (capa p&b 300px)')
reg(bw,'bg-topright',250,0,300,50); reg(bw,'bg-left',0,60,25,120); reg(bw,'sweater',190,220,280,290); reg(bw,'shirt',20,230,120,290); reg(bw,'skin-l',60,170,120,200); reg(bw,'skin-r',175,100,230,150)
l=bw@[.2126,.7152,.0722]; f=bw.reshape(-1,3); L=l.ravel()
for p in (2,10,25,50,75,90,98):
    t=np.percentile(L,p); m=np.abs(L-t)<3; print('  P',p,hx(np.median(f[m],0)))
