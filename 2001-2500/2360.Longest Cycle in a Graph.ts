function longestCycle(edges: number[]): number {
    const rank = new Array(edges.length);
    function dfs(node, acc) {
        if (node === -1 || rank[node] === -1) {
            return -1;
        } else if (rank[node] === undefined) {
            rank[node] = acc;
            const res = dfs(edges[node], acc + 1);
            rank[node] = -1;
            return res;
        } else {
            return acc - rank[node];
        }
    }
    return Math.max(...edges.map((_, i) => dfs(i, 0)));
};

