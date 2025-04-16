import matplotlib.pyplot as plt 
from matplotlib.colors import ListedColormap

def print_maze(maze):
    colors = ['red', 'black', 'white', 'green','orange']  # -1=exit, 0=wall, 1=path, 2=start, 3=frame
    cmap = ListedColormap(colors)
    plt.imshow(maze, cmap=cmap)
    plt.axis('off')
    plt.title("Maze")
    plt.show()
    return

def print_track(maze, track) : 
    for step in track :
        maze[step] = 2
    print_maze(maze)
    return