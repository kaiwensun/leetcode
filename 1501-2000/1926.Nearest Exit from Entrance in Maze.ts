function nearestExit(maze: string[][], entrance: number[]): number {
    const M = maze.length, N = maze[0].length;
    const seen = {};
    seen[entrance[0]] ||= new Set();
    seen[entrance[0]].add(entrance[1]);
    const DELTA = [-1, 0, 1, 0, -1];
    const queue = [entrance, []];
    let res = 1;
    while (queue.length > 1) {
        const point = queue.shift();
        if (point.length === 0) {
            queue.push(point);
            res++;
            continue;
        }
        for (let k = 0; k < 4; k++) {
            const di = DELTA[k], dj = DELTA[k + 1];
            const i = point[0] + di, j = point[1] + dj;
            if (!(0 <= i && i < M && 0 <= j && j < N) || maze[i][j] === "+" || seen[i]?.has(j)) {
                continue;
            }
            if (i == 0 || i == M - 1 || j == 0 || j == N - 1) {
                return res;
            }
            seen[i] ||= new Set();
            seen[i].add(j);
            queue.push([i, j]);
        }
    }
    return -1;
};

