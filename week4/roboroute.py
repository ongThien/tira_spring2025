def analyze_route(grid):
    rows = len(grid)
    cols = len(grid[0])
    g = [list(row) for row in grid]  # make mutable grid

    # Find starting position
    for i in range(rows):
        for j in range(cols):
            if g[i][j] == "R":
                r, c = i, j
                break

    g[r][c] = "."  # replace R with floor

    # Directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_idx = 0  # initially robot moves upward

    visited_cells = set()
    visited_states = set()

    while True:
        visited_cells.add((r, c))
        state = (r, c, dir_idx)

        # If we've been in the same cell with same direction before => loop
        if state in visited_states:
            return (len(visited_cells), False)
        visited_states.add(state)

        dr, dc = directions[dir_idx]
        nr, nc = r + dr, c + dc

        # If going out of bounds => exit
        if not (0 <= nr < rows and 0 <= nc < cols):
            return (len(visited_cells), True)

        # If obstacle ahead => turn right
        if g[nr][nc] == "#":
            dir_idx = (dir_idx + 1) % 4
        else:
            # move forward
            r, c = nr, nc


if __name__ == "__main__":
    grid1 = [".#......", "..#.....", ".......#", "#.R.....", "......#."]
    print(analyze_route(grid1))  # (14, True)

    grid2 = ["........", ".##.....", ".......#", "#.R.....", "......#."]
    print(analyze_route(grid2))  # (12, False)
