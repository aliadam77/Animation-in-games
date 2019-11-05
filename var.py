#declaring Width and Height
import random
Width = 1366
Height = 627
Lenght = floor(Width/300)
#answer for prompt
score = -1
minY = float("inf")
playing = True
# ifWon is making the keys not work
ifWon = False
stop = False
#Width and Height of logs and cars
logWidth = random.randint(100,120)
logHeight = 50
grassHeight = Height/9
largeHeight = Height/3
carWidth = 70
carHeight = 30
# Arrays for cars and logs
topCars = []
middleCars = []
bottomCars = []
###############
topLogs = []
middleLogs = []
bottomLogs = []
yCoord = []
#randomizing speeds of cars and logs
topCarSpeed = random.randint(1, 2)
middleCarSpeed = random.randint(1, 2)
bottomCarSpeed = random.randint(1, 2)
topLogSpeed = random.randint(1, 2)
middleLogSpeed = random.randint(1, 2)
bottomLogSpeed = random.randint(1, 2)
#setting if on the log to false
onLog = False
#colors for cars (randomized)
topColor = []
middleColor = []
bottomColor = []
#difficulty of level
difficulty = 5
#setting score to -1 because it adds 1 at start
score = 0
#if game end, cannot move keys
gameEnd = False
#side moving of keys
click  = Width/30
#setting level to 1
level = 1
lostGame = False
wonLevel = False
def goToStart():
  tx = (Width/2)-25
  ty = Height-70
  life -= 1
