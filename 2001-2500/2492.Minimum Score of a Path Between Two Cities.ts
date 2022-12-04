function minScore(n: number, roads: number[][]): number {
    const graph = {};
    for (const [a, b, distance] of roads) {
        graph[a] ||= [];
        graph[a].push([b, distance]);
        graph[b] ||= [];
        graph[b].push([a, distance]);
    }

    function dfs(node, visited, minDist) {
        let res = minDist;
        if (!visited.has(node)) {
            visited.add(node);
            for (const [neighbor, distance] of graph[node] || []) {
                res = Math.min(res, dfs(neighbor, visited, distance));
            }
        }
        return res;
    }
    const visited = new Set();
    const res = dfs(1, visited, Infinity);
    return visited.has(n) ? res : -1;
};

