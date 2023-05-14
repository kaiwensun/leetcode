function maxMoves(grid: number[][]): number {
    const M = grid.length, N = grid[0].length;
    let dpPre: number[] = new Array(M).fill(0);
    let dpCur: number[] = new Array(M);
    let res = 0;
    for (let j = 1; j < N; j++) {
        for (let i = 0; i < M; i++) {
            dpCur[i] = Math.max(...[
                i > 0 && grid[i - 1][j - 1] < grid[i][j] ? dpPre[i - 1] + 1 : -Infinity,
                grid[i][j - 1] < grid[i][j] ? dpPre[i] + 1 : -Infinity,
                i < M - 1 && grid[i + 1][j - 1] < grid[i][j] ? dpPre[i + 1] + 1 : -Infinity 
            ]);    
        }
        res = Math.max(res, ...dpCur);
        const tmp = dpPre; dpPre = dpCur; dpCur = tmp;
    }
    return res;
};

