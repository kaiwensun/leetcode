int countServers(int** grid, int gridSize, int *gridColSize){
    int* rowCnt = (int*)malloc(gridSize * sizeof(int));
    memset(rowCnt, 0, gridSize * sizeof(int));
    int* colCnt = (int*)malloc(*gridColSize * sizeof(int));
    memset(colCnt, 0, *gridColSize * sizeof(int));
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < *gridColSize; j++) {
            if (grid[i][j]) {
                rowCnt[i]++;
                colCnt[j]++;
            }
        }
    }
    int res = 0;
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < *gridColSize; j++) {
            res += (rowCnt[i] > 1 || colCnt[j] > 1) && grid[i][j];
        }
    }
    free(rowCnt);
    free(colCnt);
    return res;
}
