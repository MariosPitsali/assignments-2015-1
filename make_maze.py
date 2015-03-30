import random
import sys


visited_cells = []
log = []


def find_valid_neighbors(cell, n):
    neighbors = []

    for x in range(cell[0] - 1, cell[0] + 2):
        # Check whether "x" lies inside the maze
        if x < 0 or x >= n:
            continue
        for y in range(cell[1] - 1, cell[1] + 2):
            current = (x, y)
            # Check whether "x" lies inside the maze or if we are dealing
            # with "cell" itself (x == cell[0] and y == cell[1])
            if y < 0 or y >= n or (current == cell):
                continue
            # Reject diagonal neighboring
            if not (x == cell[0]) and not (y == cell[1]):
                continue
            # Check if we have already visited this cell
            if current not in visited_cells:
                neighbors.append(current)

    return neighbors


def get_random_neighbor(neighbors):
    return random.choice(neighbors)


def visit_cell(cell, n):
    visited_cells.append(cell)


def find_next_cell(cell, n):
    neighbors = find_valid_neighbors(cell, n)

    if len(neighbors) == 0:
        return None

    return get_random_neighbor(neighbors)


def run_maze_step(current_cell, n):
    visit_cell(current_cell, n)
    next_cell = find_next_cell(current_cell, n)
    if next_cell:
        log.append((current_cell, next_cell))
        run_maze_step(next_cell, n)


if __name__ == '__main__':
    n = int(sys.argv[1])
    start_x = int(sys.argv[2])
    start_y = int(sys.argv[3])
    input_seed = int(sys.argv[4])
    output_file_path = sys.argv[5]

    random.seed(input_seed)

    # Run maze
    start = (start_x, start_y)
    run_maze_step(start, n)

    with open(output_file_path, 'w') as output_file:
        for line in log:
            output_file.write('%s, %s\n' % (line[0], line[1]))
