function maximumDetonation(bombs: number[][]): number {
    const dist = (b1, b2) => (b1[0] - b2[0]) ** 2 + (b1[1] - b2[1]) ** 2;
    const N = bombs.length;
    const graph = Array(N);
    bombs.forEach((bomb1, i) => {
        graph[i] = [];
        bombs.forEach((bomb2, j) => {
            if (i !==j && dist(bomb1, bomb2) <= bomb1[2] ** 2) {
                graph[i].push(j);
            }
        });
    });
    const dfs = (i, visited) => visited[i] ? 0 : (visited[i] = true) && 1 + graph[i].reduce((sum, j) => sum + dfs(j, visited), 0);
    return Math.max(...(graph.map((_, i) => dfs(i, {}))));
};

