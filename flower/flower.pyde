def setup():
    global cx, cy 
    size (500,500)
    colorMode(RGB)     
    cx = width/2
    cy = height/2
    
cx = 0
xy = 0   
r = 150 
j = 1
        
def draw():
    global cx, cy
    global r
    num = 14
    theta = TWO_PI / 14
    
    background(100, 180, 190)
    noStroke()
    strokeWeight(0.5)
    for j in range(20):
        r = j * 12
        a = j * 3
        for i in range(num):
            angle = theta * i
            c = (i / float(num)) * 255
            print(c)
            fill(242,242,242)
            
            x = cx + sin(angle) * r
            y = cy + cos(angle) * r
            stroke(200,200,201)
          #  line(cx,cy,x,y)
            stroke(200,200,200)
            circle(x, y, 130)
            fill(255,174,66)
            stroke(255,174,66)
            ellipse (250, 250, 45, 45)
            fill(123, 189, 0)
            ellipse (250, 250, 40, 40)
