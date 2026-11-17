import sys, numpy as np, colorsys
from PIL import Image
hx=lambda c:'#%02x%02x%02x'%tuple(int(round(v)) for v in c)
def load(p): return np.asarray(Image.open(p).convert('RGB')).astype(float)
def reg(a,n,x0,y0,x1,y1):
    r=a[y0:y1,x0:x1].reshape(-1,3); print(f'  {n:14s} med {hx(np.median(r,0))} mean {hx(r.mean(0))}')
bw=load(sys.argv[1]); co=load(sys.argv[2])
print('DIA (capa p&b 300px)')
reg(bw,'bg-topright',250,0,300,50); reg(bw,'bg-left',0,60,25,120); reg(bw,'sweater',190,220,280,290); reg(bw,'shirt',20,230,120,290); reg(bw,'skin-l',60,170,120,200); reg(bw,'skin-r',175,100,230,150)
l=bw@[.2126,.7152,.0722]; f=bw.reshape(-1,3); L=l.ravel()
for p in (2,10,25,50,75,90,98):
    t=np.percentile(L,p); m=np.abs(L-t)<3; print('  P',p,hx(np.median(f[m],0)))
print('NOITE (foto colorida 400x500)')
reg(co,'bg-top',150,0,260,20); reg(co,'bg-right',385,100,400,200); reg(co,'sweater',250,330,390,470); reg(co,'shirt',5,350,60,470)
reg(co,'skin-l',60,260,160,300); reg(co,'skin-r',250,100,340,170); reg(co,'hair-r',230,30,330,60); reg(co,'hair-l',60,130,170,150)
f=co.reshape(-1,3)[::5]; hsv=np.array([colorsys.rgb_to_hsv(*(p/255)) for p in f]); l=f@[.2126,.7152,.0722]
def sel(n,m): print(' ',n,int(m.sum()),hx(np.median(f[m],0)) if m.sum() else '-')
sel('stripe red',(hsv[:,0]<.04)|(hsv[:,0]>.96)); 
sel('red bright',((hsv[:,0]<.04)|(hsv[:,0]>.96))&(hsv[:,1]>.5)&(hsv[:,2]>.45))
sel('maroon',((hsv[:,0]<.04)|(hsv[:,0]>.96))&(hsv[:,1]>.5)&(hsv[:,2]>.18)&(hsv[:,2]<.4))
sel('skin',(hsv[:,0]>.04)&(hsv[:,0]<.1)&(hsv[:,1]>.25)&(hsv[:,2]>.6))
sel('skin shadow',(hsv[:,0]>.03)&(hsv[:,0]<.1)&(hsv[:,1]>.3)&(hsv[:,2]>.3)&(hsv[:,2]<.6))
sel('black',l<22); sel('white',l>240)
