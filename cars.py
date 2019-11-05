#drawing cars
from var import*
import random
topLane = Height/5*3
middleLane = Height/7*5
bottomLane = Height/6*5

def goToStart(tx,ty,score):
    tx = (Width//2)-25
    ty = Height-70
    score = 0
    return tx,ty,score

def drawCar (x,y,lane,index):
    pushMatrix()
    #putting x and y coordinates in different locations
    translate(x, y)
    noStroke()
    #wheel Width, x and y of coordinates
    wheelWidth = 20
    wheelHeight = 20
    wheelX = carWidth/3.5
    wheelY = carHeight/2 - wheelWidth/5
    rectMode(CENTER)
    
    #drawing wheels
    fill(255);
    rect(-wheelX, wheelY, wheelWidth, wheelHeight, 7)
    rect(wheelX, wheelY, wheelWidth, wheelHeight, 7)
    rect(-wheelX, -wheelY, wheelWidth, wheelHeight, 7)
    rect(wheelX, -wheelY, wheelWidth, wheelHeight, 7)
    #fill colors for each car row
    if (lane == topLane):
        fill(topColor[index])
    elif (lane == middleLane):
        fill(middleColor[index])
    else:
        fill(bottomColor[index])
	
    #drawing rectangle
    rect(0, 0, carWidth, carHeight, 8)
    fill(0, 0, 0)
    rectMode(CORNER)
    popMatrix()

#drawing cars
def doCars(tx,ty,dt,score):
    for i in range(Lenght):
        topCars[i] += topCarSpeed*dt;
        #changing color every time it goes through screen
        if (topCars[i] > Width):
            topCars[i] = -carWidth/2
        #topColor[i] = color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        drawCar(topCars[i], Height/5*3, 'top', i)
        #detecting if it is hitting the car, then go to start
        if (tx <= topCars[i] + 35  and tx + 85 >= topCars[i]  and ty <= Height/5*3 + 15  and ty + 65 >= Height/5*3):
            tx,ty,score= goToStart(tx,ty,score)

    #same for other cars
    for i in range(0,Lenght):
        middleCars[i] = (middleCars[i] - middleCarSpeed*dt)
        if (middleCars[i] < 0):
            middleCars[i] = Width
        #middleColor[i] = color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        drawCar(middleCars[i], Height/7*5, 'middle', i)
        if (tx <= middleCars[i] + 35 and tx + 85 >= middleCars[i] and ty <= Height/7*5 + 15 and ty + 65 >= Height/7*5):    
            tx,ty,score = goToStart(tx,ty,score)
			
    for i in range(Lenght):
        bottomCars[i] += bottomCarSpeed*dt
        if (bottomCars[i] > Width):
            bottomCars[i] = -carWidth/2
        #bottomColor[i] =color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        drawCar(bottomCars[i], Height/6*5, 'bottom', i)
        if (tx <= bottomCars[i] + 35  and tx + 85 >= bottomCars[i]  and ty <= Height/6*5 + 15  and ty + 65 >= Height/6*5):
            tx,ty,score = goToStart(tx,ty,score)
    return tx,ty,score
