from var import*
import random
def RRT(dt,tx,ty,tree):
    s = "up"
    tau =1
    tempx = tx
    tempy = ty
    for i in range(1,tau+1):
        if tempy == 558 or tempy == 557:
            tempx,tempy = bottomGrass(dt,tempx,tempy,s,i,tree)
        elif tempy == 489 or tempy == 490 or tempy == 488:
            tempx,tempy = bottomLaneCollision(dt,tempx,tempy,s,i,tree)
        elif tempy == 419 or tempy == 420:
            tempx,tempy = middleLaneCollision(dt,tempx,tempy,s,i,tree)
        elif tempy == 350 or tempy == 351:
            tempx,tempy = topLaneCollision(dt,tempx,tempy,s,i,tree)
        elif tempy == 281 or tempy == 282:
            tempx,tempy = middleGrass(dt,tempx,tempy,s,i,tree)
        elif tempy == 212 or tempy == 213:
            tempx,tempy = bottomRiver(dt,tempx,tempy,s,i,tree)
        elif tempy == 143 or tempy == 144:
            tempx,tempy =middleRiver(dt,tempx,tempy,s,i,tree)
        elif tempy == 74 or tempy == 75:
           tempx,tempy = topRiver(dt,tempx,tempy,s,i,tree)
        else:
            # print(tempy)
             tree.append("stay")
            
    return tempx,tempy

def reGrow(dt,tx,ty,tree):
    tempx = tx
    tempy = ty
    s = "up"
    tau =1
    for i in range(1,tau+1):
        if tempy == 558 or tempy == 557:
            tempx,tempy = bottomGrass(dt,tempx,tempy,s,i,tree)
        elif tempy == 489 or tempy == 490 or tempy == 488:
            tempx,tempy = bottomLaneCollision(dt,tempx,tempy,s,i,tree)
        elif tempy == 419 or tempy == 420:
            tempx,tempy = middleLaneCollision(dt,tempx,tempy,s,i,tree)
        elif tempy == 350 or tempy == 351:
            tempx,tempy = topLaneCollision(dt,tempx,tempy,s,i,tree)
        elif tempy == 281 or tempy == 282:
            tempx,tempy = middleGrass(dt,tempx,tempy,s,i,tree)
        elif tempy == 212 or tempy == 213:
            tempx,tempy = bottomRiver(dt,tempx,tempy,s,i,tree)
        elif tempy == 143 or tempy == 144:
            tempx,tempy =middleRiver(dt,tempx,tempy,s,i,tree)
        elif tempy == 74 or tempy == 75:
           tempx,tempy = topRiver(dt,tempx,tempy,s,i,tree)
        else:
            # print("said")
            tempy+=0
            tempx+=0
            tree.append("stay")
    return tempx, tempy

def topRiver(dt,x,y,s,i,tree):
    if s == "up":
         tree.append("up")
         y -= grassHeight
    return x,y
def middleRiver(dt,x,y,s,i,tree):
    if s == "up":
        for j in range(Lenght):
            if (x > topLogs[j]+topLogSpeed*dt*i - logWidth / 2  and x < topLogs[j]+topLogSpeed*dt*i  + logWidth / 2  and y - grassHeight > (Height / 6 - 5) - logHeight  and y - grassHeight < (Height / 6 - 5) + logHeight / 2) :
                tree.append("up")
                y -= grassHeight
                return x,y
        tree.append("stay")
    return x,y

def bottomRiver(dt,x,y,s,i,tree):
    if s == "up":
        for j in range(Lenght):
            if (x > middleLogs[j]-middleLogSpeed*dt*i - logWidth / 2  and x < middleLogs[j]-middleLogSpeed*dt*i + logWidth / 2  and y - grassHeight > (Height/4+10) - logHeight  and y - grassHeight < (Height/4+10) + logHeight / 2):
                tree.append("up")
                y -= grassHeight
                return x,y
        tree.append("stay")
    return x,y


def middleGrass(dt,x,y,s,i,tree):
    if s == "up":
        for j in range(Lenght):
           if (x > bottomLogs[j]+bottomLogSpeed*dt*i - logWidth / 2  and x < bottomLogs[j]+bottomLogSpeed*dt*i + logWidth / 2  and y- grassHeight> (Height/8*3) - logHeight  and y - grassHeight < (Height/8*3) + logHeight / 2):
                tree.append("up")
                y -= grassHeight
                return x,y
        tree.append("stay")
    return x,y
            

def topLaneCollision(dt,x,y,s,i,tree):
    if s == "up":        
        tree.append("up")
        y-=grassHeight
        return x,y
        
    elif x == "left":
        for j in range(Lenght):
            if (x - click <= topCars[j]+topCarSpeed*dt*i + 35  and x - click + 85 >= topCars[j]+topCarSpeed*dt   and y <= Height/5*3 + 15  and y + 65 >= Height/5*3):
                topLaneCollision(dt,x,y,"right",i,tree)
                return x,y
        tree.append("left")
        x -= click
        
        
    elif s == "right":
        for j in range(Lenght):
            if (x + click <= topCars[j]+topCarSpeed*dt*i + 35  and x + click + 85 >= topCars[j]+topCarSpeed*dt   and y <= Height/5*3 + 15  and y + 65 >= Height/5*3):
                topLaneCollision(dt,x,y,"down",i,tree)
                return x,y
        tree.append("right")
        x += click
        
    elif s == "down":
        for j in range(Lenght):
            if (x <= middleCars[j]+middleCarSpeed*dt*i + 35 and x + 85 >= middleCars[j]+middleCarSpeed*dt*i and y+ grassHeight <= Height/7*5 + 15 and y+ grassHeight + 65 >= Height/7*5):
                tree.append("stay")
        tree.append("down")
        y+=grassHeight
    return x,y
def middleLaneCollision(dt,x,y,s,i,tree):
    if s == "up":
        for j in range(Lenght):
            if (x <= topCars[j]+topCarSpeed*dt*i + 35  and x + 85 >= topCars[j]+topCarSpeed*dt   and y - grassHeight <= Height/5*3 + 15  and y - grassHeight + 65 >= Height/5*3):
                middleLaneCollision(dt,x,y,"left",i,tree)
                return x,y
        tree.append("up")
        y-=grassHeight
    elif s == "left":
        for j in range(Lenght):
            if (x - click <= middleCars[j]+middleCarSpeed*dt*i + 35 and x - click + 85 >= middleCars[j]+middleCarSpeed*dt*i and y <= Height/7*5 + 15 and y + 65 >= Height/7*5):
                middleLaneCollision(dt,x,y,"right",i,tree)
                return x,y
        tree.append("left")
        x -= click
        
    elif s == "right":
        for j in range(Lenght):
            if (x + click <= middleCars[j]+middleCarSpeed*dt*i + 35 and x + click + 85 >= middleCars[j]+middleCarSpeed*dt*i and y <= Height/7*5 + 15 and y + 65 >= Height/7*5):
                middleLaneCollision(dt,x,y,"down",i,tree)
                return x,y
        tree.append("right")
        x += click
    elif s == "down":
        for j in range(Lenght):
            if (x <= bottomCars[j]+bottomCarSpeed*dt*i + 35  and x + 85 >= bottomCars[j]+bottomCarSpeed*dt*i  and y+ grassHeight <= Height/6*5 + 15  and y+ grassHeight + 65 >= Height/6*5):
                tree.append("stay")
        tree.append("down")
        y+=grassHeight
            
    return x,y

def bottomLaneCollision(dt,x,y,s,i,tree):
    if s == "up":
        for j in range(Lenght):
            if (x <= middleCars[j]+middleCarSpeed*dt*i + 35  and x + 85 >= middleCars[j]+middleCarSpeed*dt   and y - grassHeight <= Height/7*5 + 15  and y - grassHeight + 65 >= Height/7*5):
                bottomLaneCollision(dt,x,y,"right",i,tree)
                return x,y
        tree.append("up")
        y -= grassHeight
    elif s == "left":
        for j in range(Lenght):
            if (x - click <= bottomCars[j]+bottomCarSpeed*dt*i + 35 and x - click + 85 >= bottomCars[j]+bottomCarSpeed*dt*i and y <= Height/6*5 + 15 and y + 65 >= Height/6*5):
                bottomLaneCollision(dt,x,y,"bottom",i,tree)
                return x,y
        tree.append("left")
        x -= click
        
    elif s == "right":
        for j in range(Lenght):
            if (x + click <= bottomCars[j]+bottomCarSpeed*dt*i + 35 and x + click + 85 >= bottomCars[j]+bottomCarSpeed*dt*i and y <= Height/6*5 + 15 and y + 65 >= Height/6*5):
                bottomLaneCollision(dt,x,y,"left",i,tree)
                return x,y
        tree.append("right")
        x += click
    elif s == "down":
            tree.append("down")
    return x,y
def bottomGrass(dt,x,y,s,i,tree):
    if s == "up":
        for j in range(Lenght):
            if (x <= bottomCars[j]+bottomCarSpeed*dt*i + 35 and x + 85 >= bottomCars[j]+bottomCarSpeed*dt*i and y - grassHeight <= Height/6*5 + 15 and y - grassHeight + 65 >= Height/6*5):
                r = random.random()
                if r>0.5:
                    tree.append("left")
                    x -= click
                    return x,y
                else:
                    tree.append("right")
                    x += click
                    return x,y
        tree.append("up")
        y-=grassHeight
    return x,y
