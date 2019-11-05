from cars import*
from logs import*
from var import*
from RRT import*
#x & y pos of character
guyX = (Width/2)-(Width/54.43)
guyY = Height-(Height/9)
tx = guyX
ty = guyY
tree = []
tempx =0
tempy= 0
score =0
flag = False
delay = 0
def setup () :
    size(Width, Height)
    global tx
    global ty
    global guyX
    global guyY
    global tree
    global tempx
    global tempy
    #loading images
    global avatar
    avatar = loadImage("Sonic.png")
    #setting up topcars
    for i in range(Lenght):
        #putting the cars anywhere between these coordinates
        topCars.append(Width*i/Lenght + random.randint(-Width/12, Width/12))
        #random.randint colors
        topColor.append(color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    
    #setting up middlecars
    for i in range(Lenght):
        #putting the cars anywhere between these coordinates
        middleCars.append(Width*i/Lenght + random.randint(-Width/12, Width/12))
        #random.randint colors
        middleColor.append(color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    
    #setting up bottomcars
    for i in range(Lenght):
        #putting the cars anywhere between these coordinates
        bottomCars.append(Width*i/Lenght + random.randint(-Width/12, Width/12))
        #random.randint colors
        bottomColor.append(color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    
    #same for all logs, and random.randintly placing between coordinates
    for i in range(Lenght):
        topLogs.append( Width*i/Lenght + random.randint(-100, 100))
    for i in range(Lenght):
        middleLogs.append( Width*i/Lenght + random.randint(-100, 100))
    for i in range(Lenght):
        bottomLogs.append( Width*i/Lenght + random.randint(-100, 100))
    tempx,tempy = RRT(0.5,tx,ty, tree)
    

def draw() :
    global tx
    global ty
    global guyX
    global guyY
    global tree
    global tempx
    global tempy
    global score
    global flag
    global delay
    noStroke() 
    background(255,255,255) 
    drawGrass() 
    fill(0,0,0) 
    #road
    fill(0,0,0) 
    rect(0, 2 * grassHeight + largeHeight, Width, largeHeight) 
    #water
    fill(135,206,250) 
    rect(0, grassHeight, Width, largeHeight) 
    
    #road lines
    for i in range(0,Width,40):
        stroke (255,255,255) 
        line (i, 1.38 * largeHeight + 1.88 * grassHeight, i + 25, 1.38* largeHeight + grassHeight*1.88) 
        line (i, 1.62 * largeHeight + 2.12 * grassHeight, i + 25, 1.62 * largeHeight + grassHeight*2.12)
        
    tx,ty,score =theLogs(tx,ty,0.5,score) 
    tx,ty,score = doCars(tx,ty,0.5,score) 
    textSize(20) 
    fill(0,0,0) 
    
    textSize(20) 
    text("Score: " + str(score), 60, height/20) 
    
    guyX = lerp(guyX, tx, 0.6) 
    guyY = lerp(guyY, ty, 0.6) 
    image(avatar, guyX, guyY, 50, 50) 
    
    if flag == False:
        if delay> 25:
            flag = True
        else:
            delay+=1
    else:
        if len(tree)>0:
            s = tree.pop(0)
            tx,ty,score = moveAgent(score,s,tx,ty,guyX,guyY)  
            tempx,tempy =reGrow(0.5,tx,ty,tree)
            flag = False
            delay = 0
    
def moveAgent(score,s,tx,ty,guyX,guyY) :
    if s == "up":
        if(guyY > 50):
            ty -= grassHeight;
            score += 1;
    if (s == "s"):
        if (guyY < Height-80):
            ty += grassHeight
            score += 1;
    if (s == "left"):
        if(guyX > 50):
            tx -= click
            score += 1;
                
    if (s == "right"):
        if(guyX < Width-85):
            tx += click
            score += 1;
    if s == "stay":
        # print(ty)
        # print("stay")
        tx+=0
        ty+=0
    return tx,ty,score
                
#going to the start of the program
