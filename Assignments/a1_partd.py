#    Main Author(s): Hanbi Gong
#    Main Reviewer(s):

from a1_partc import Queue

def get_overflow_list(grid):
    overflow_cells = []
    rows = len(grid)
    cols = len(grid[0])

    for x in range(rows):
        for y in range(cols):
            neighbor_count = sum(1 for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)] 
                                 if 0 <= x + dx < rows and 0 <= y + dy < cols)

            if abs(grid[x][y]) >= neighbor_count:
                overflow_cells.append((x, y))

    return overflow_cells if overflow_cells else None

def overflow(grid, a_queue):
    iterations = 0

    while True:
        if all(cell >= 0 for row in grid for cell in row) or all(cell <= 0 for row in grid for cell in row):
            return iterations

        cells_to_overflow = get_overflow_list(grid)

        if not cells_to_overflow:
            return iterations

        is_positive = grid[cells_to_overflow[0][0]][cells_to_overflow[0][1]] >= 0

        for i, j in cells_to_overflow:
            grid[i][j] = 0

        for i, j in cells_to_overflow:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                    if is_positive:
                        grid[ni][nj] = abs(grid[ni][nj]) + 1
                    else:
                        grid[ni][nj] = -abs(grid[ni][nj]) - 1

        a_queue.enqueue([row[:] for row in grid])
        iterations += 1


