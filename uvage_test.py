import uvage

XSIZE = 600
YSIZE = 600

camera = uvage.Camera(XSIZE, YSIZE)
pyImage = uvage.from_image(XSIZE/2,YSIZE/2,"https://www.python.org/static/img/python-logo@2x.png")
speedx = 8
speedy = 8

def tick():
    global speedx
    global speedy
    camera.clear("black")
    pyImage.x += speedx
    pyImage.y += speedy
    if pyImage.x > 400 or pyImage.x < 200:
        speedx *= -1
    if pyImage.y > 550 or pyImage.y < 50:
        speedy *= -1
    camera.draw(pyImage)
    camera.display()

uvage.timer_loop(30, tick)