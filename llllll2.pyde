x = 0
def setup():
    size(550,700)
    colorMode(HSB,255)
def draw():
    global x
    img = loadImage("hg.jpg")
    image(img,0,0)
    fill(x,255,255)
    ellipse(250,450,270,270)
    ellipse(150,300,100,150)
    ellipse(350,300,100,150)
    ellipse(200,600,100,150)
    ellipse(300,600,100,150)
    if x == 255:
        x = 0
        
    x += 1
