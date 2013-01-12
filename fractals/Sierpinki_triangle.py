import pygame, sys
from pygame.locals import *
#midpoint of the line
def midpoint(p1, p2):
    return((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
#timer intialize
clock = pygame.time.Clock()
#initialize screen
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Sierpinki triangle')
#main loop
def main():
    while 1:
        screen.fill((0,0,0))
        pygame.draw.polygon(screen, (255,0,0),((100,450),(500,450),(300,104)))
        points = [[(100,450),(500,450),(300,104)]]
        pygame.display.update()
        clock.tick(1)
        for k in range(1,8,1):
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            array = []
            for point in points:
                l = []
                for i in range(0,3,1):
                    first = midpoint(point[i-1],point[i])
                    second = midpoint(point[i],point[(i+1)%3])
                    pygame.draw.line(screen,(255,255,0),first,second,1)
                    l += [[first,point[i],second]]
                array += l
            points = array
            pygame.display.update()
            clock.tick(1)


if __name__ == '__main__': main()
