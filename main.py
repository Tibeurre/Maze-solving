import numpy as np
import random as rd
import generating as g
import misc as m
import printing as p

def right_hand_solving(maze):
    start = tuple(np.argwhere(maze == 2)[0])
    previous = (0,0)
    current = start

    track = []

    while maze[current] != -1 :
        track.append(current)
        neighbors = m.sorted_neighbors(maze,current,previous)
        previous = current
        current = neighbors[0]
    
    return track

def mouse_solving(maze):

    start = tuple(np.argwhere(maze == 2)[0])
    current = start
    track = []

    while maze[current] != -1 :
        track.append(current)
        neighbors = m.get_neighbors(maze, current)
        current = rd.choice(neighbors)
    
    return track

def Tremaux_solving(maze):

    maze_marking = maze.copy()

    start = tuple(np.argwhere(maze == 2)[0])
    current = start
    previous = (0,0)
    track = []

    while maze[current] != -1 :
        track.append(current)
        neighbors = m.get_neighbors(maze)
        if len(neighbors)>2:
            neighbors.remove(previous) ...


maze = g.generate(50)
p.print_track(maze, right_hand_solving(maze))