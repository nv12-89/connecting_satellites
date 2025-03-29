import pgzrun, random
from random import randint
import time
WIDTH=800
HEIGHT=600
TITLE="Catching Game Key Events"

alien_1=Actor("positive_alien")
alien_2=Actor("negative_alien")
catcher=Actor("lifeguard_zombie")

alien_1.pos=randint(50,WIDTH-50),randint(50,HEIGHT-50)
alien_2.pos=randint(50,WIDTH-50),randint(50,HEIGHT-50)

def draw():
        


pgzrun.go()