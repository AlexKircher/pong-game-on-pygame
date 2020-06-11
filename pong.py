import pygame
import math

Weight = 600
Height = 600
BorderYU=1
BorderYD=1
BorderXD=0.01*Weight
BorderXU=Weight-0.01*Weight
R=0
B=200
class RK (object):
    def __init__(self,color,x,y=None):
        self.color=color
        self.x=x
        self.y=y
        self.w=20
        self.h=120
        self.dy=0
        self.info=[self.x,self.y,self.w,self.h]
    def moveP (self, syt):
        if(syt==False):
            if(self.dy>0):
                self.dy-=0.25
            elif(self.dy<0):
                self.dy+=0.25
        if(self.info[1]<BorderYD and self.dy>0):
            self.info[1]+=self.dy
            if self.info[1]>BorderYD:
                self.info[1]=BorderYD
                
        if(self.info[1]>BorderYU and self.dy<0):
            self.info[1]+=self.dy
            if self.info[1]<BorderYU:
                self.info[1]=BorderYU
        
class Ball (object):
    def inint_(self,color,x,y):
        self.x=x
        self.y=y
        self.color = color
        self.r=20
        self.ax=7
        self.ay=0
        self.live=True
    def moveB (self):
        self.x+=self.ax
        self.y+=self.ay
        if (self.y>BorderYD+120 and self.ay>0):
            self.ay=-1*self.ay
            self.y=round(BorderYD+120)
            
        elif (self.y<BorderYU and self.ay<0):
            self.ay=-1*self.ay
            
            self.y=round(BorderYU)
        if (self.x<BorderXD+20 and self.ax<0):
            self.live = False
            self.x=round(BorderXD)
        elif (self.x>BorderXU-20 and self.ax>0):
            self.live=False 
            self.x=round(BorderXU)
    def coliderB (self, xRK,yRK,h,ayRK):
        if ((abs(xRK-self.x) <=30)and(abs(self.y-yRK-60)<=70)):
            self.ax+=1
            self.ax=-1*self.ax
            self.ay= round((ayRK+self.ay)/2)  #max(abs(round(ayRK)),abs(self.ay))
            
            
            
                
                
        
      
    def draw (self):
        
        pygame.draw.circle(sc, (0,255,100), (self.x, self.y), 15)
        
pygame.init ();

sc=pygame.display.set_mode((Weight, Height))
pygame.display.set_caption("PONG")
WHITE=(255,255,255)
RED=(255,0,0)
BLACK=(0,0,0)
GREEN=(0,255,0)

Player= RK(GREEN,10,360)
PlayerB= RK(GREEN,590,360)
#Player.init_(RK,BLACK,10,300)
#PlayerB=RK
#PlayerB.init_(RK,BLACK,570,300)
shar = Ball
shar.inint_(Ball,RED,300,300)
BorderYU=Height*0.01
BorderYD=Height-Height*0.01-Player.h
game = True;
FPS = 30

sy=False
syb = False
clock=pygame.time.Clock()
while game:
    while shar.live:
        clock.tick(FPS)
        for i in pygame.event.get():
         if i.type == pygame.QUIT:
            pygame.quit()
            game=False
         elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_w :
                Player.dy=-9
                sy=True
            elif i.key == pygame.K_s :
                sy=True
                Player.dy=9
         
            if i.key == pygame.K_UP :
                PlayerB.dy=-9
                syb=True
                
            elif i.key == pygame.K_DOWN :
                syb=True
                PlayerB.dy=9
         elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_w, pygame.K_s]:
                sy=False
         elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_UP, pygame.K_DOWN]:
                syb=False
        sc.fill(BLACK)
        Player.moveP(sy)
        PlayerB.moveP(syb)
        
        shar.coliderB(shar,Player.x,Player.info[1],Player.h,Player.dy)
        shar.coliderB(shar,PlayerB.x,PlayerB.info[1],PlayerB.h,PlayerB.dy)

        shar.moveB(shar)
        shar.draw(shar)
        pygame.draw.rect(sc,PlayerB.color,(PlayerB.info[0]-20,PlayerB.info[1],PlayerB.info[2],PlayerB.info[3]))
        pygame.draw.rect(sc,Player.color,Player.info)
        
        pygame.display.update()
        
    for i in pygame.event.get():
        if i.type == pygame.KEYDOWN:
            if i.key in [pygame.K_w,pygame.K_UP]:
                shar.live=True
        elif i.type == pygame.QUIT:
            pygame.quit()
            game=False
        
    Player.y=80
    shar.x=300
    shar.y=300
    shar.ay=0
    shar.ax=7
    f1 = pygame.font.Font(None, 68)
    sc.fill((0,200,0))
    restart = f1.render('Press UP for start', 1, (R, 0, B))
    sc.blit(restart,(125,300))
    R=200-R
    B=200-B
    pygame.display.update()
    
 
    
    
