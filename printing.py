import matplotlib.pyplot as plt 
from matplotlib.colors import ListedColormap

def print_maze(maze):
    colors = ['lime', 'black', 'white', 'green','orange','yellow','lime']  # -1=exit, 0=wall, 1=path, 2=start, 3=frame
    cmap = ListedColormap(colors)
    plt.imshow(maze, cmap=cmap)
    plt.axis('off')
    plt.title("Maze")
    plt.show()
    return

def print_track(maze, track) : 
    for step in track :
        maze[step] = 4
    opti_path = reconstruct_optimal_path(track)
    for step in opti_path :
        maze[step] = 5
    print_maze(maze)
    return

from collections import deque

def reconstruct_optimal_path(trace):
    '''ChatGPT'''
    visited_set = set(trace)
    start = trace[0]
    end = trace[-1]
    
    # Pour backtracking plus tard
    parents = {}

    # BFS inversé
    queue = deque([end])
    parents[end] = None  # fin n’a pas de parent

    while queue:
        current = queue.popleft()
        
        if current == start:
            break  # chemin trouvé

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:  # voisinage 4 directions
            neighbor = (current[0] + dx, current[1] + dy)

            if neighbor in visited_set and neighbor not in parents:
                parents[neighbor] = current
                queue.append(neighbor)
    
    # Reconstruire le chemin
    path = []
    current = start
    while current is not None:
        path.append(current)
        current = parents[current]
    
    return path  # déjà dans le bon ordre (start → end)
