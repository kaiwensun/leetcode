int DELTA[] = {-2, -1, 1, 2};

bool next(int** grid, int gridSize, int* cur) {
    for (int i = 0; i < 4; i++) {
        int x = cur[0] + DELTA[i];
        if (x < 0 || x >= gridSize) continue;
        for (int j = 0; j < 4; j++) {
            if (i + j == 3 || i == j) continue;
            int y = cur[1] + DELTA[j];
            if (y < 0 || y >= gridSize) continue;
            if (grid[cur[0]][cur[1]] + 1 == grid[x][y]) {
                cur[0] = x;
                cur[1] = y;
                return true;
            }
        }
    }
    return false;
}

bool checkValidGrid(int** grid, int gridSize, int* gridColSize){
    if (grid[0][0] != 0) return false;
    int cur[] = {0, 0};
    for (int i = 1; i < gridSize * gridSize; i++) {
        if (!next(grid, gridSize, cur)) {
            return false;
        }
    }
    return true;
}

