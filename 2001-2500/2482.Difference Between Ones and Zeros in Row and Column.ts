function onesMinusZeros(grid: number[][]): number[][] {
    const rowOnes = grid.map(row => row.reduce((acc, n) => acc + n, 0))
    const colOnes = grid[0].map((_, j) => grid.reduce((acc, row) => acc + row[j], 0));
    const diff = new Array(grid.length);
    for (let i = 0; i < grid.length; i++) {
        diff[i] = new Array(grid[i].length);
        for (let j = 0; j < grid[i].length; j++) {
            diff[i][j] = rowOnes[i] + colOnes[j] - (grid[i].length - rowOnes[i] + grid.length - colOnes[j]);
        }
    }
    return diff;
};

