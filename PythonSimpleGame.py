###IMPORTANT THIS CODE WAS WRITTEN FOR TRINKET HERE IS A LINK TO THE WORKING INTERPRETER https://trinket.io/turtle###
###THIS CODE WILL NOT FUNCTION PROPERLY ON A REGULAR INTERPRETER###


import turtle, random, math
theo = turtle.Turtle()
apple = turtle.Turtle()
screen = theo.getscreen()
theo.penup()
apple.penup()

def hitBox(x, y):
  theo.goto(x, y)
  theo.speed(1000)
  theo.pendown()
  theo.fillcolor('blue')
  theo.begin_fill()
  for i in range(0, 4):
    theo.forward(50)
    theo.right(90)
  theo.penup()
  theo.end_fill()

def apples(x, y):
  apple.goto(x, y)
  apple.speed(100)
  apple.pendown()
  apple.fillcolor('green')
  apple.begin_fill()
  apple.circle(10)
  apple.penup()
  apple.end_fill()
  
x = 0
y = 0

ax = random.randint(0, 200)
ay = random.randint(0, 200)

score = 0

while True:
  
  distance = math.sqrt(((ax-x)**2)+((ay-y)**2))
  
  #print(distance)
  
  #print(rangex, rangey)
  #print(x, y)
  #print(ax, ay)
  
  hitBox(x, y)
  usrInput = str(input())
  if usrInput.lower() == 'a':
    for i in range(0, 2):
      x = x - 10
      theo.clear()
      apple.clear()
  
  if usrInput.lower() == 'd':
    for i in range(0, 2):
      x = x + 10
      theo.clear()
      apple.clear()
      
  if usrInput.lower() == 'w':
    for i in range(0, 2):
      y = y + 10
      theo.clear()
      apple.clear()
      
  if usrInput.lower() == 's':
    for i in range(0, 2):
      y = y - 10
      theo.clear()
      apple.clear()
  
  if distance < 30:
    ax = random.randint(0, 200)
    ay = random.randint(0, 200)
    score = score + 1
    print(score)
  
  hitBox(x, y)
  apples(ax, ay)