function findMaxFish(grid: number[][]): number {
    const M = grid.length, N = grid[0].length;
    const DELTA = [-1, 0, 1, 0, -1];
    function dfs(i: number, j: number): number {
        if (i < 0 || i >= M || j < 0 || j >= N || grid[i][j] === 0) return 0;
        let res = grid[i][j];
        grid[i][j] = 0;
        for (let k = 0; k < 4; k++) {
            res += dfs(i + DELTA[k], j + DELTA[k + 1]);
        }
        return res;
    }
    let res = 0;
    for (let i = 0; i < M; i++) {
        for (let j = 0; j < N; j++) {
            res = Math.max(res, dfs(i, j));
        }
    }
    return res;
};

