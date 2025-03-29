import pgzrun
from random import randint
import time
WIDTH=800
HEIGHT=600
TITLE="Connecting the Satellites"

satellites=[]

n=randint(5,10)

for i in range(n):
    s=Actor("satellite")
    s.pos=randint(50, WIDTH-80), randint(50,HEIGHT-80)
    satellites.append(s)

def draw():
    for i in range (n):
        satellites[i].draw()
        screen.draw.text(str(i+1),(satellites[i][0],satellites[i][1]),fontsize=50,color="black")
    
    # for i in satellites:
    #     i.draw() 
    # screen.draw.text(str(i+1),(satellites[i][0],satellites[i][1]),fontsize=50,color="black")


pgzrun.go()