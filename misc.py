import numpy as np

def get_neighbors (maze, current):
    x, y = current
    neighbors = []

    if x > 0 and (maze[x-1,y] == 1 or maze[x-1,y] == -1) :
        neighbors.append((x-1,y))
    if x < maze.shape[0]-1 and (maze[x+1,y] == 1 or maze[x+1,y] == -1):
        neighbors.append((x+1,y))
    if y > 0 and (maze[x,y-1] == 1 or maze[x,y-1] == -1) :
        neighbors.append((x,y-1))
    if y < maze.shape[1]-1 and (maze[x,y+1] == 1 or maze[x,y+1] == -1) :
        neighbors.append((x,y+1))
    
    return neighbors    

def sorted_neighbors(maze,current,previous):

    neighbors = []
    diffed = (current[0]-previous[0], current[1]-previous[1])
    x, y = current

    if diffed[0] > 0 :
        if y > 0 and (maze[x,y-1] == 1 or maze[x,y-1] == -1) :
            neighbors.append((x,y-1))
        if x < maze.shape[0]-1 and (maze[x+1,y] == 1 or maze[x+1,y] == -1):
            neighbors.append((x+1,y))
        if y < maze.shape[1]-1 and (maze[x,y+1] == 1 or maze[x,y+1] == -1) :
            neighbors.append((x,y+1))
        if x > 0 and (maze[x-1,y] == 1 or maze[x-1,y] == -1):
            neighbors.append((x-1,y))

    elif diffed[0] < 0 :
        if y < maze.shape[1]-1 and (maze[x,y+1] == 1 or maze[x,y+1] == -1) :
            neighbors.append((x,y+1))
        if x > 0 and (maze[x-1,y] == 1 or maze[x-1,y] == -1) :
            neighbors.append((x-1,y))
        if y > 0 and (maze[x,y-1] == 1 or maze[x,y-1] == -1) :
            neighbors.append((x,y-1))
        if x < maze.shape[0]-1 and (maze[x+1,y] == 1 or maze[x+1,y] == -1):
            neighbors.append((x+1,y))
    
    elif diffed[1] > 0 :
        if x < maze.shape[0]-1 and (maze[x+1,y] == 1 or maze[x+1,y] == -1):
            neighbors.append((x+1,y))
        if y < maze.shape[1]-1 and (maze[x,y+1] == 1 or maze[x,y+1] == -1) :
            neighbors.append((x,y+1))
        if x > 0 and (maze[x-1,y] == 1 or maze[x-1,y] == -1) :
            neighbors.append((x-1,y))
        if y > 0 and (maze[x,y-1] == 1 or maze[x,y-1] == -1) :
            neighbors.append((x,y-1))

    elif diffed[1] < 0: 
        if x > 0 and (maze[x-1,y] == 1 or maze[x-1,y] == -1) :
            neighbors.append((x-1,y))
        if y > 0 and (maze[x,y-1] == 1 or maze[x,y-1] == -1) :
            neighbors.append((x,y-1))
        if x < maze.shape[0]-1 and (maze[x+1,y] == 1 or maze[x+1,y] == -1):
            neighbors.append((x+1,y))
        if y < maze.shape[1]-1 and (maze[x,y+1] == 1 or maze[x,y+1] == -1) :
            neighbors.append((x,y+1))
    
    return neighbors