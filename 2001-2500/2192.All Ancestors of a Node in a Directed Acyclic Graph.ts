function getAncestors(n: number, edges: number[][]): number[][] {
    const graph = {};
    for (const [from, to] of edges) {
        graph[to] ||= [];
        graph[to].push(from);
    }
    const res = Array(n);
    function ancestors(node): number[] {
        if (res[node] === undefined) {
            res[node] = [];
            for (const from of graph[node] || []) {
                res[node].push(parseInt(from));
                res[node] = res[node].concat(ancestors(from));
            }
            res[node] = res[node].sort((a, b) => parseInt(a) - parseInt(b)).filter((num, i) => res[node][i] != res[node][i + 1]);
        }
        return res[node];
    }
    for (let i = 0; i < n; i++) {
        ancestors(i);
    }
    return res;
};

