#define max(a,b) ((a) > (b) ? (a) : (b))

int sum(int** grid, int i, int j) {
    return grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1] + grid[i][j] + grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1];
}

int maxSum(int** grid, int gridSize, int* gridColSize){
    int res = 0;
    for (int i = 1; i < gridSize - 1; i++) {
        for (int j = 1; j < gridColSize[i] - 1; j++) {
            res = max(res, sum(grid, i, j));
        }
    }
    return res;
}

