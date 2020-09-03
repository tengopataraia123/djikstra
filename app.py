import pygame
import time

EMPTY = 0
WALL = 1
POINT = 2
CHECKED = 3
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Block():
    def __init__(self,code=EMPTY):
        self.code = code
        self.path = ""

def draw_grid(surface,grid):

    for x in range(40):
        for y in range(30):
            if(grid[x][y].code == POINT):
                pygame.draw.rect(surface,RED,(x*20,y*20,20,20))
            elif(grid[x][y].code == WALL):
                pygame.draw.rect(surface,BLUE,(x*20,y*20,20,20))
            elif(grid[x][y].code == CHECKED):
                pygame.draw.rect(surface,GREEN,(x*20,y*20,20,20))            

    for x in range(41):
        pygame.draw.line(surface,BLACK,(x*20,0),(x*20,600))
    for y in range(31):
        pygame.draw.line(surface,BLACK,(0,y*20),(800,y*20))

def find_path(points,grid,surface):
    check = [points[0]]
    newCheck = []
    
    found = False
    
    #grid[points[0][0]][points[0][1]].code = CHECKED
    
    while not found:    
    #make check list
        for p in check:
            oldx,oldy = p
            if(p[0]-1 >= 0):
                x,y = (p[0]-1,p[1])
                if grid[x][y].code != CHECKED and (x,y) not in newCheck and grid[x][y].code != WALL:
                    newCheck.append((x,y))
                    grid[x][y].path = grid[oldx][oldy].path+"l"
            if(p[0]+1 < 40):
                x,y = (p[0]+1,p[1])
                if grid[x][y].code != CHECKED and (x,y) not in newCheck and grid[x][y].code != WALL:
                    newCheck.append((x,y))
                    grid[x][y].path = grid[oldx][oldy].path+ "r"
            if(p[1]-1 >= 0):
                x,y = (p[0],p[1]-1)
                if grid[x][y].code != CHECKED and (x,y) not in newCheck and grid[x][y].code != WALL:
                    newCheck.append((x,y))
                    grid[x][y].path = grid[oldx][oldy].path+ "u"
            if(p[1]+1 < 30):
                x,y = (p[0],p[1]+1)
                if grid[x][y].code != CHECKED and (x,y) not in newCheck and grid[x][y].code != WALL:
                    newCheck.append((x,y))
                    grid[x][y].path = grid[oldx][oldy].path+ "d"
            
        check = newCheck
        newCheck = []
         #check
        for t in check:
            if(t == points[1]):
                found = True
            elif(t != points[0]):
                grid[t[0]][t[1]].code = CHECKED
        draw_grid(surface,grid)
        pygame.display.flip()
        time.sleep(0.07)
    return found

def draw_path(surface,points,grid):
    x,y = points[0]
    x = x*20+10
    y = y*20+10
    nx,ny = x,y
    
    path = grid[points[1][0]][points[1][1]].path
    
    for d in path:
        if d == "l":
            nx = x-20
        elif d == "r":
            nx = x+20
        elif d == "u":
            ny = y-20
        elif d == "d":
            ny = y+20
        pygame.draw.line(surface,RED,(x,y),(nx,ny),3)
        x = nx
        y = ny
    
def main():

    pygame.init()
    window = pygame.display.set_mode((800,600))

    running = True

    clock = pygame.time.Clock()

    grid = []
    for row in range(40):
        column = []
        for col in range(30):
            block = Block()
            column.append(block)
        grid.append(column)
        
    points = []
    
    window.fill((255,255,255))
    
    drawing = False
    found = False

    while running:

        for evnt in pygame.event.get():
            if evnt.type == pygame.QUIT:
                running = False
            elif evnt.type == pygame.KEYDOWN:
                if evnt.key == pygame.K_ESCAPE:
                    running = False
                elif evnt.key == pygame.K_SPACE:
                    found = find_path(points,grid,window)
                elif evnt.key == pygame.K_r:
                    grid = []
                    for row in range(40):
                        column = []
                        for col in range(30):
                            block = Block()
                            column.append(block)
                        grid.append(column)
                        
                    points = []
                    
                    window.fill((255,255,255))
                    
                    drawing = False
                    found = False
                    
            elif evnt.type == pygame.MOUSEBUTTONDOWN:
                if len(points) != 2:
                    x,y = pygame.mouse.get_pos()
                    x = int(x/20)
                    y = int(y/20)
                    grid[x][y].code = POINT
                    points.append((x,y))
                else:
                    drawing = True
            elif evnt.type == pygame.MOUSEBUTTONUP:
                drawing = False
        if drawing:
            x,y = pygame.mouse.get_pos()
            x = int(x/20)
            y = int(y/20)
            grid[x][y].code = WALL            
        
        draw_grid(window,grid)
        
        if found:
            draw_path(window,points,grid)        
        
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()