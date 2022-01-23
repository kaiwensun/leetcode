function highestRankedKItems(grid: number[][], pricing: number[], start: number[], k: number): number[][] {
    const [M, N] = [grid.length, grid[0].length];
    const DELTA = [1, 0, -1, 0, 1];

    function getReachableProdDist() {
        const dist = Array(M);
        for (let i = 0; i < M; i++) dist[i] = [];
        dist[start[0]][start[1]] = 0;
        const reachable = [start];
        const prod = [];
        let p = -1;
        while (++p < reachable.length) {
            let cur = reachable[p];
            let [i, j] = [cur[0], cur[1]];
            if (pricing[0] <= grid[i][j] && grid[i][j] <= pricing[1]) {
                prod.push(cur);
            }
            for (let k = 0; k < 4; k++) {
                let x = i + DELTA[k];
                let y = j + DELTA[k + 1];
                if (!(0 <= x && x < M && 0 <= y && y < N)) continue;
                if (grid[x][y] === 0) continue;
                if (dist[x][y] !== undefined) continue;
                dist[x][y] = dist[i][j] + 1;
                reachable.push([x, y]);
            }
        }
        return {prod, dist};
    }

    function compare([x1, y1], [x2, y2]) {
        return dist[x1][y1] - dist[x2][y2] || grid[x1][y1] - grid[x2][y2] || x1 - x2 || y1 - y2;
    }

    const {prod, dist} = getReachableProdDist();
    return prod.sort(compare).slice(0, k);

};

