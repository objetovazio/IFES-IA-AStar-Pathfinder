from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import time
import sys
from numpy import random


def load_maze(filename):
    """read sent file of a string matrix and convert it into a matrix structure"""
    file = open(filename, "r")
    line = file.readline()

    size_line = 0
    size_column = len(line.rstrip("\n").split(" "))

    maze = []
    while line:
        size_line += 1
        list_line = line.rstrip("\n").split(" ")  # Remove /n
        # Change 0 to 1; Change 1 to 0;
        line_int = [1 if pos == '0' else 0 for pos in list_line]
        maze.append(line_int)
        line = file.readline()
    # end

    print('maze size %d lines %d columns' % (size_line, size_column))

    return maze
# end-load_maze()


def str_to_axis(str_axis):
    """Transform a string of axis "0,0" to a tuple of (0, 0)"""
    axis_pos = str_axis.split(",")
    axis_int = (int(axis_pos[1]), int(axis_pos[0]))
    return axis_int
# end-str_to_axis()

# get a random axis that was not used and is walkable


def get_axis(evaluated_set, size_x, size_y, grid):
    axis = None
    # get a axis that was not used yet
    while(axis == None):
        axis = (random.randint(size_x), random.randint(size_y))

        if(axis not in evaluated_set and grid.walkable(axis[0], axis[1])):
            evaluated_set.append(axis)
            node_axis = grid.node(axis[0], axis[1])
        else:
            axis = None
        #end-while()
    #end-while()

    return node_axis
#end get_axis()


def main():
    # get params from sys
    filename = sys.argv[1]
    start = sys.argv[2]
    end = sys.argv[3]

    # get axis params
    start = str_to_axis(start)
    end = str_to_axis(end)

    # load maze into a matrix
    maze = load_maze(filename)

    # instantiate lib pathfinding components #
    # grid (maze matrix)
    grid = Grid(matrix=maze)

    # start and end nodes existing on the grid
    start = grid.node(start[0], start[1])
    end = grid.node(end[0], end[1])

    # instantiate finder and run
    finder = AStarFinder(diagonal_movement=DiagonalMovement.always)

    start_time = time.time()
    path, runs = finder.find_path(start, end, grid)
    end_time = time.time() - start_time

    print('operations:', runs, 'path length:', len(path), 'execution time:', end_time)
    print(grid.grid_str(path=path, start=start, end=end))
    print('path:', path)
# end-main()

if __name__ == '__main__':
    main()
