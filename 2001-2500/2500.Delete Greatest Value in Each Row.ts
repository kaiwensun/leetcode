function deleteGreatestValue(grid: number[][]): number {
    grid.forEach(row => row.sort((a, b) => a - b));
    let res = 0;
    for (let j = 0; j < grid[0].length; j++) {
        let max = -Infinity;
        for (let i = 0; i < grid.length; i++) {
            max = Math.max(max, grid[i][j]);
        }
        res += max;
    }
    return res;
};

