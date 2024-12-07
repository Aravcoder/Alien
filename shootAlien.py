import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 500
TITLE = "Shoot the Alien"

message = ""
alien = Actor('alien')
alien.pos = 50,50
def draw():
    screen.clear()
    screen.fill(color="Blue")
    alien.draw()
pgzrun.go()    