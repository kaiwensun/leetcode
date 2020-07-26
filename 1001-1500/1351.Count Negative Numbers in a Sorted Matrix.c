

int countNegatives(int** grid, int gridSize, int* gridColSize){
    int cnt = 0;
    for (int i = gridSize - 1; i >= 0; i--) {
        if (grid[i][gridColSize[i] - 1] >= 0) break;
        for (int j = gridColSize[i] - 1; j >= 0; j--)
            if (grid[i][j] < 0) cnt += 1;
            else if (grid[i][j] > 0) break;
    }
    return cnt;
}

