function maxPoints(grid: number[][], queries: number[]): number[] {
    const M = grid.length, N = grid[0].length;
    const UFData = new Array(M);
    for (let i = 0; i < M; i++) {
        UFData[i] = new Array(N);
        for (let j = 0; j < N; j++) {
            UFData[i][j] = [i, j, 1];
        }
    }
    function find(i, j) {
        const res = UFData[i][j];
        if (res[0] !== i || res[1] != j) {
            UFData[i][j] = find(res[0], res[1]);
        }
        return UFData[i][j];
    }
    function union(i, j, x, y) {
        const res1 = find(i, j);
        const res2 = find(x, y);
        if (res1 !== res2) {
            UFData[res1[0]][res1[1]] = res2;
            res2[2] += res1[2];
        }
    }
    function flowTo(i, j) {
        const DELTA = [1, 0, -1, 0, 1];
        for (let k = 0; k < 4; k++) {
            const x = i + DELTA[k], y = j + DELTA[k + 1];
            if (x < 0 || x >= M || y < 0 || y >= N) continue;
            if (grid[i][j] < grid[x][y]) continue;
            union(i, j, x, y);
        }
    }
    const coords = [];
    let coordsIter = 0;
    for (let i = 0; i < M; i++) for (let j = 0; j < N; j++) coords.push([i, j]);
    coords.sort((a, b) => grid[a[0]][a[1]] - grid[b[0]][b[1]]);
    return queries
        .map((q, i) => [q, i])
        .sort((a, b) => a[0] - b[0])
        .map(([q, i]) => {
            while(coordsIter < coords.length && grid[coords[coordsIter][0]][coords[coordsIter][1]] < q) {
                flowTo(coords[coordsIter][0], coords[coordsIter][1]);
                coordsIter++;
            }
            return [q > grid[0][0] ? find(0, 0)[2] : 0, i];
        })
        .sort((a, b) => a[1] - b[1])
        .map(([ans, i]) => ans);
};

