function checkXMatrix(grid: number[][]): boolean {
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid.length; j++) {
            if ((i === j || grid.length - 1 - i === j) === !grid[i][j]) {
                return false;
            }
        }
    }
    return true;
};

