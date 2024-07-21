
import pgzrun
import random

#system variables for window size

WIDTH = 300
HEIGHT = 300

#system function

def draw():
    print('window created')
    rWidth = WIDTH
    rHeight = 100
    rColor = random.randint(100,255)
    gColor = 255
    bColor = 0
    for i in range(20):
        ret = Rect((0,0),(rWidth,rHeight))
        ret.center = (150,150)
        screen.draw.rect(ret,(rColor,gColor,bColor))
        rWidth -= 10
        rHeight += 10
        gColor -= 10
        bColor += 10

pgzrun.go()

