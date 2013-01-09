# import modules
import pygame,sys
from pygame.locals import *

#setup the colors
GREEN = (0, 100, 0)
ORENGE = (255, 102, 0)
GREY = (120, 120,120)

#initialise screen
pygame.init() # initialize pygame
screen=pygame.display.set_mode((635,480)) #setup the window
pygame.display.set_caption("Conway's Game of Life")
screen.fill(GREY)

#drawing grid
for j in range(0,640,22):
     for i in range(0,480,22):
         pygame.draw.rect(screen,(ORENGE),pygame.Rect(j,i,20,20))

#drawing green cells
pixObj=pygame.PixelArray(screen)
pixObj[132:152,88:108]=GREEN
pixObj[154:174,88:108]=GREEN
pixObj[176:196,88:108]=GREEN
pixObj[110:130,110:130]=GREEN
pixObj[132:152,110:130]=GREEN
pixObj[154:174,110:130]=GREEN

m=44
for m in range(44, 90, 22):
    for n in range(44,90,22):   
        pixObj[m:m+20,n:n+20]=GREEN

#checking neighbours
def main():
    while 1:
        for c in range(10,400,22):
            for r in range(10,400,22):  
                count=0
                if pixObj[c,r-22]==screen.map_rgb(GREEN):
                    count=count+1
                if pixObj[c,r+22]==screen.map_rgb(GREEN):
                    count +=1
                if pixObj[c-22,r-22]==screen.map_rgb(GREEN):
                    count +=1
                if pixObj[c-22,r]==screen.map_rgb(GREEN):
                    count+=1
                if pixObj[c-22,r+22]==screen.map_rgb(GREEN):
                    count+=1
                if pixObj[c+22,r-22]==screen.map_rgb(GREEN):
                    count+=1
                if pixObj[c+22,r]==screen.map_rgb(GREEN):
                    count+=1
                if pixObj[c+22,r+22]==screen.map_rgb(GREEN):
                    count+=1
                #conditions
                if pixObj[c,r]==screen.map_rgb(GREEN):
                    if count<2 or count>3:
                        pixObj[c-10:c+10,r-10:r+10]=(ORENGE)
                    else:
                        pixObj[c-10:c+10,r-10:r+10]=(GREEN)
                if pixObj[c,r]==screen.map_rgb(ORENGE):
                    if count==3:
                        pixObj[c-10:c+10,r-10:r+10]=(GREEN)
     
                pygame.display.update()

        for event in pygame.event.get():
	    if event.type==QUIT:			
	        pygame.quit()
		sys.exit()
            elif event.type== KEYDOWN and event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == '__main__':main()

