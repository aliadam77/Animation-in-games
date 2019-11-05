from var import*
def goToStart(tx,ty,score):
    tx = (Width//2)-25
    ty = Height-70
    score = 0
    return tx,ty,score

def drawLogs(logX,logY,logLane,logIndex):
  pushMatrix() 
  translate(logX, logY) 
  noStroke() 
  rectMode(CENTER) 
  fill(139,69,19)  
  rect(0, 0, logWidth, logHeight, 7) 
  rectMode(CORNER) 
  popMatrix() 

#drawing grass
def drawGrass():
  #bottom grass
  fill (62,124,70) 
  rect(0, 2 * grassHeight + 2 * largeHeight, Width, grassHeight) 
  #middle grass
  fill (238,214,175) 
  rect(0, grassHeight + largeHeight, Width, grassHeight) 
  #top grass
  rect(0, 0, Width, grassHeight) 
  
def theLogs(tx,ty,dt,score):
    #checking if it is in the water
    if (ty > (grassHeight - largeHeight / 3)+70  and ty < (grassHeight - largeHeight / 3) + largeHeight+70) :
        #it is off the log
        onLog = False
    else :
        #otherwise, setting the guy on the log
        onLog = True
	
    #drawing toplogs
    for i in range(Lenght):
        #speed and going back to beginning
        topLogs[i] = (topLogs[i] + topLogSpeed*dt) % Width 
        #drawing logs
        drawLogs(topLogs[i], Height/6-5, 'top', i) 
        #if on the log, increment the speed of the guyY to the speed of the log, and on the log is true
        if (tx > topLogs[i] - logWidth / 2  and tx < topLogs[i]  + logWidth / 2  and ty > (Height / 6 - 5) - logHeight  and ty < (Height / 6 - 5) + logHeight / 2) :
            tx += topLogSpeed*dt
            onLog = True
		
	
    #drawing bottomlogs 
    for i in range(Lenght):
        bottomLogs[i] = (bottomLogs[i] + bottomLogSpeed*dt) % Width 
        #drawing logs
        drawLogs(bottomLogs[i], Height/8*3, 'bottom', i) 
        #if on the log, increment the speed of the guyY to the speed of the log, and on the log is true
        if (tx > bottomLogs[i] - logWidth / 2  and tx < bottomLogs[i] + logWidth / 2  and ty > (Height/8*3) - logHeight  and ty < (Height/8*3) + logHeight / 2):
            tx += bottomLogSpeed*dt
            onLog = True
	
    #drawing middlelogs 
    for i in range(Lenght):
        middleLogs[i] = (middleLogs[i] - middleLogSpeed*dt) 
        if (middleLogs[i] < 0):
            middleLogs[i] = Width 
        #drawing logs
        drawLogs(middleLogs[i], Height/4+10, 'middle', i)
        #if on the log, increment the speed of the guyY to the speed of the log, and on the log is true
        if (tx > middleLogs[i] - logWidth / 2  and tx < middleLogs[i] + logWidth / 2  and ty > (Height/4+10) - logHeight  and ty < (Height/4+10) + logHeight / 2):
            tx -= middleLogSpeed*dt
            onLog = True
            

        #if it is not on the log, it go to the original coordinares
    if (onLog == False):
        tx,ty,score =goToStart(tx,ty,score)
    return tx,ty,score
