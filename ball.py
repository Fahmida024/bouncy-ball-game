import pgzrun
import random
TITLE='bouncy bouncy'
WIDTH=800
HEIGHT=600
GRAVITY=2000.0

class Ball:
    def __init__(self,x1,y1,r1,c1):
        self.x=x1
        self.y=y1
        self.r=r1
        self.c=c1
        self.vx=200
        self.vy=0


    def draw(self):
        screen.draw.filled_circle((self.x, self.y),self.r, self.c )

ball=Ball(50,100,40,'purple')
ball2=Ball(30,60,20,'blue')
def draw():
    screen.clear()
    ball.draw()
    ball2.draw()
    

def update(dt):
    uy = ball.vy
    ball.vy+=GRAVITY*dt
    ball.y+=(uy+ball.vy)*0.5*dt
    if ball.y > 600:
        ball.y=550
        ball.vy=-ball.vy*0.9
    ball.x+=ball.vx*dt
    if ball.x>750 or ball.x<50:
        ball.vx=-ball.vx
    uy=ball.vy
    ball.vy+=GRAVITY*dt
    ball.y+=(uy+ball.vy)*0.5*dt

    uy = ball2.vy
    ball2.vy+=GRAVITY*dt
    ball2.y+=(uy+ball2.vy)*0.5*dt
    if ball2.y > 600:
        ball2.y=550
        ball2.vy=-ball2.vy*0.7
    ball2.x+=ball2.vx*dt
    if ball2.x>750 or ball2.x<50:
        ball2.vx=-ball2.vx
    uy=ball2.vy
    ball2.vy+=GRAVITY*dt
    ball2.y+=(uy+ball2.vy)*0.5*dt

def on_key_down(key):
    if key==keys.SPACE:
        ball.vy=-500
    if key==keys.UP:
        ball2.vy=-400






    







pgzrun.go()

        
