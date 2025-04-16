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


maze = g.generate(90)
p.print_track(maze, mouse_solving(maze))