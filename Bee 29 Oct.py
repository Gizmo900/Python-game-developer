import pgzrun
from random import randint
WIDTH=600
HEIGHT=500
score=0
game_over=False
bee=Actor("bee")
bee.pos = 150,200
flower=Actor ("flower")
flower.pos=134,208
def draw():
    screen.blit("backround",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("score:"+str(score),color = "yellow",topleft = (10,10))
    if game_over == True: 
        screen.fill("sky blue")
        screen.draw.text("game over you have scored:"+str(score),color = "green",fontsize = 40,topleft = (10,10))


def update():
    global score
    if keyboard.left :
        bee.x-=3
    if keyboard.right:
        bee.x+=3
    if keyboard.up:
        bee.y-=3
    if keyboard.down:
        bee.y+=3

    if bee.colliderect(flower):
        score+=1
        flower.pos=randint(50,450),randint(50,450)

def timer():
    global game_over
    game_over = True

clock.schedule(timer,60)
pgzrun.go()


















