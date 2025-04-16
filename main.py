import numpy as np
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

maze = g.generate(90)
p.print_track(maze, right_hand_solving(maze))