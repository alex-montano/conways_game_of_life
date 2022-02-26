from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time
import tracemalloc

x_lim, y_lim = 47, 17
mat = np.zeros([y_lim, x_lim])
loop = False

neighbors = [
    [-1, -1],   # top-left
    [0, -1],    # top-mid
    [1, -1],    # top-right
    [-1, 0],    # mid-left
    [1, 0],     # mid-right
    [-1, 1],    # bot-left
    [0, 1],     # bot-mid
    [1, 1]      # bot-right
]

# to right
mat[10, 41] = 1
mat[10, 42] = 1
mat[11, 40] = 1
mat[11, 41] = 1
mat[11, 42] = 1
mat[11, 43] = 1
mat[12, 40] = 1
mat[12, 41] = 1
mat[12, 43] = 1
mat[12, 44] = 1
mat[13, 42] = 1
mat[13, 43] = 1

def init():
    mat = np.zeros([y_lim, x_lim])

def update(z):
    print(z)
    cells_to_kill = []
    cells_to_revive = []
    
    for i in range(x_lim):
        for j in range(y_lim):
            # checks if kill the actual cell:
            # - overpopulation: >3 living neighbors cells.
            # - underpopulation: <2 living neighbors cells.
            if mat[j, i] == 1:
                living_cells = 0
                for k, coord in enumerate(neighbors):
                    try:
                        if mat[j - coord[1], i - coord[0]] == 1:
                            living_cells += 1
                        if living_cells > 3:
                            cells_to_kill.append([j, i])
                            break
                        if k + 1 == len(neighbors) and living_cells < 2:
                            cells_to_kill.append([j, i])
                    except IndexError:
                        pass
                        
            # checks if revive the actual cell:
            # - be a dead cell and has 3 neighbors alive
            else:
                living_cells = 0
                for k, coord in enumerate(neighbors):
                    try:
                        if mat[j - coord[1], i - coord[0]] == 1:
                            living_cells += 1
                        if k + 1 == len(neighbors) and living_cells == 3:
                            cells_to_revive.append([j, i])
                    except IndexError:
                        pass
                        
    # kill or revive the cells marked
    for cell in cells_to_kill:
        mat[cell[0], cell[1]] = 0
    for cell in cells_to_revive:
        mat[cell[0], cell[1]] = 1
        
    plot.set_array(mat)

if __name__ == '__main__':
    fig, ax = plt.subplots()
    ax.set_axis_off()
    plot = plt.matshow(
        mat,
        fignum=0,
        cmap='cividis'
    )
    animation = FuncAnimation(
        fig,
        update,
        init_func = init,
        interval = 100,
    )
    plt.show()
    