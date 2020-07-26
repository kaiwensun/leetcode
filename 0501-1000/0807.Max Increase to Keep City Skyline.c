#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))

int maxIncreaseKeepingSkyline(int** grid, int gridSize, int* gridColSize){
    int rowMax[gridSize];
    int colMax[gridColSize[0]];
    memset(rowMax, 0, gridSize * sizeof(int));
    memset(colMax, 0, gridColSize[0] * sizeof(int));
    int res = 0;
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridColSize[i]; j++) {
            rowMax[i] = MAX(rowMax[i], grid[i][j]);
            colMax[j] = MAX(colMax[j], grid[i][j]);
        }
    }
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridColSize[i]; j++) {
            res += MIN(rowMax[i], colMax[j]) - grid[i][j];
        }
    }
    return res;
}
