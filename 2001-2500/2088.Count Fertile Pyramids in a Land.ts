function countPyramids(grid: number[][]): number {
    const n = grid[0].length;
    function countDirectionalPyramids(delta: number) {
        let start = delta == 1 ? 0 : grid.length - 1;
        let end = delta == 1 ? grid.length : -1;
        let res = 0;
        let prevRow = Array(n).fill(0);
        for (let i = start; i !== end; i += delta) {
            const row = Array(n);
            row[0] = grid[i][0];
            for (let j = 1; j < n - 1; j++) {
                if (grid[i][j] === 0) {
                    row[j] = 0;
                } else {
                    row[j] = 1 + Math.min(prevRow[j - 1], prevRow[j], prevRow[j + 1]);
                    res += row[j] - 1;
                }
            }
            row[n - 1] = grid[i][n - 1];
            prevRow = row;
        }
        return res;
    }
    return countDirectionalPyramids(1) + countDirectionalPyramids(-1);
};

