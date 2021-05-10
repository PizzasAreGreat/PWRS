#modules
import pygame
from time import *
from random import *
from playsound import *
import threading
print("  _______ _      _____       _            ")
print(" |__   __| |    |  __ \     (_)           ")
print("    | |  | |    | |__) |     _ _ __   ___ ")
print("    | |  | |    |  _  /     | | '_ \ / __|")
print("    | |  | |____| | \ \     | | | | | (__ ")
print("    |_|  |______|_|  \_\    |_|_| |_|\___|")
print("                     TLR inc")
print("////////////// /!\logiciel sous credits/!\ /////////////////")
print("////////////////////////ver 0.4/////////////////////////////")
sleep(3)
#variables
print("initialisation of the variables")
#background variables
red=(204,0,0)
dark_red=(163,0,0)
green=(0,125,0)
dark_green=(0,100,0)
alarm_mute=False
#gameplay-related variables
coretemp=0
loop1=325
loop2=310
loop3=260
rods=0
corepressure=0
exchangertemp=0
waterlevel=100
#waterlevel : 0 to 100 %
rodfailure=False
loop1failure=False
loop2failure=False
loop3failure=False
loop1completefailure=False
loop2completefailure=False
loop3completefailure=False
meltdown=False
explosion=False
coriumreachingground=False
gameover=False
loop1pump1=True
loop1pump2=True
loop2pump1=True
loop2pump2=True
loop3pump1=True
loop3pump2=True
print("initialisation of the UI")
#startup
pygame.init() 
res = (720, 720)
screen = pygame.display.set_mode(res)
color=(255,255,255)
color_light=(170,170,170)
color_dark=(100,100,100)
#window.fill((184, 191, 194))
width=screen.get_width()
height=screen.get_height()
smallfont = pygame.font.SysFont('Corbel',35) 
text = smallfont.render('quit' , True , color) 
screen.fill((184, 191, 194))
#pygame.display.update()  
#functions and UI
LOOP1PUMP1BUTTON = (height / 4, width / 3, 140, 40, "pump1") 
LOOP1PUMP2BUTTON = (height / 4, 2 * width / 3, 140, 40, "pump 2")
LOOP2PUMP1BUTTON = (2 * height / 4, width / 3, 140, 40, "pump1")
LOOP2PUMP2BUTTON = (2 * height / 4, 2 * width / 3, 140, 40, "pump2")
LOOP3PUMP1BUTTON = (3 * height / 4, width / 3, 140, 40, "pump1")
LOOP3PUMP2BUTTON = (3 * height / 4, 2 * width / 3, 140, 40, "pump2")
def loopfailures(pump1, pump2):
    if pump1 is True and pump2 is True:
        return "Safe"
    elif pump1 is False and pump2 is False:
        return "complete failure"
    else:
        return "failure"

def failures(var, message1):
  #print("//////////", message1, " info //////////")
  if var is True:
    print(message1)
  else:
    print(message1, ": safe", sep = "")

def drawLoopButtons(width, height, size1, size2, text):
    touchingbutton = width <= mouse[0] <= width + size1 and height <= mouse[1] <= height + size2
    
    if touchingbutton is True: 
        pygame.draw.rect(screen, dark_green, [width , height ,140,40])
    else: 
        pygame.draw.rect(screen, green, [width, height,140,40])
    
    screen.blit(text , (int(width) + 50, height))

def failurecheck() :
    if  loop1failure is True or loop1completefailure is True or loop2failure is True or loop2completefailure is True or loop3failure is True or loop3completefailure is True :
        return True
    else :
        return False

def gameaudio():
 if  failurecheck() is True:
   playsound('failure.mp3')


    
# welcome message
input("Welcome to the PWRS, the Pressurized Water Reactor Simulator, a realistic nuclear reactor simulator on python \n which gives to the user a very complete control of the main reactor features \n we perfectly know that this simulation might lack some feature that would seriously increse it's \n realism, but please keep in mind that this is a beta version. \n press enter to start the simulation")
playsound('systemready.mp3')
#audio management thread startup
class audioThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)

  def run(self):
    gameaudio()

audioThread = audioThread()
audioThread.start()
#main loop
while gameover is False :
  #routines de protection des variables
  if rods > 100 :
    rods=100
  if rods < 0 :
      rods = 0
  if waterlevel > 100 :
      waterlevel = 100
  if waterlevel < 0 :
      waterlevel = 0
  print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
  print("//////////water system status/////////")
  print("loop 1:", loopfailures(loop1pump1, loop1pump2))
  print("loop 2:", loopfailures(loop2pump1, loop2pump2))
  print("loop 3:", loopfailures(loop3pump1, loop3pump2))
  print("///loop 1:")
  if loop1pump1 is True:
      print("pump 1 : safe")
  else :
      print("pump 1 : offline/failure")
  if loop1pump2 is True:
      print("pump 2 : safe")
  else :
      print("pump 2 : offline/failure")
  print("///loop 2:")
  if loop2pump1 is True:
      print("pump 1 : safe")
  else :
      print("pump 1 : offline/failure")
  if loop2pump2 is True:
      print("pump 2 : safe")
  else :
      print("pump 2 : offline/failure")
  print("///loop 3:")
  if loop3pump1 is True:
      print("pump 1 : safe")
  else :
      print("pump 1 : offline/failure")
  if loop3pump2 is True:
      print("pump 2 : safe")
  else :
      print("pump 2 : offline/failure")
  print("//////////////core info///////////////")
  print("core temperature:", coretemp ," °C")
  print("core pressure:", corepressure)
  print(waterlevel, "%")
  print("//////////////rods info///////////////")
  print("rods height:", rods)
  if rodfailure is True:
      print("rods: Failure")
  else:
      print("rods: Safe")
  print("/////////////Failures info//////////////////")
  failures(meltdown, "Meltdown")
  failures(explosion, "explosion")
  failures(coriumreachingground, "corium reaching ground")
  mouse = pygame.mouse.get_pos() 
  touchingbuttonl1p1 = LOOP1PUMP1BUTTON[0] <= mouse[0] <= LOOP1PUMP1BUTTON[0] +LOOP1PUMP1BUTTON[2] and LOOP1PUMP1BUTTON[1] <= mouse[1] <= LOOP1PUMP1BUTTON[1] + LOOP1PUMP1BUTTON[3]
  for ev in pygame.event.get(): 
    if ev.type == pygame.QUIT: 
        pygame.quit() 
    #checks if the mouse is clicked 
    if ev.type == pygame.MOUSEBUTTONDOWN: 

        if touchingbuttonl1p1 is True: 
            if loop1pump1 is True :
                loop1pump1=False
            else : 
                loop1pump1=True 
  screen.fill((184, 191, 194))
  drawLoopButtons(LOOP1PUMP1BUTTON[0], LOOP1PUMP1BUTTON[1], LOOP1PUMP1BUTTON[2], LOOP1PUMP1BUTTON[3], LOOP1PUMP1BUTTON[4])
  pygame.display.update() 

#gameover sequence
playsound('failure.mp3')
 
"""

"""
