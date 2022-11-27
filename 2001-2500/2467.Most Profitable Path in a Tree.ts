function mostProfitablePath(edges: number[][], bob: number, amount: number[]): number {
    function makeGraph() {
        const graph = {};
        for (const [u, v] of edges) {
            graph[u] ||= [];
            graph[u].push(v);
            graph[v] ||= [];
            graph[v].push(u);
        }
        return graph;
    }
    let meetPoint = undefined;
    function clearB(graph) {
        function dfs(node: number, from: number, depth: number) {
            if (node === bob) {
                amount[bob] = 0;
                return depth;
            }
            let bobDepth = 0;
            for (const child of graph[node]) {
                if (child === from) continue;
                bobDepth = Math.max(bobDepth, dfs(child, node, depth + 1));
                if (bobDepth) {
                    if (depth * 2 === bobDepth) {
                        amount[node] /= 2;
                    } else if (depth * 2 > bobDepth) {
                        amount[node] = 0;
                    }
                    break;
                };
            }
            return bobDepth;
        }
        dfs(0, -1, 0);
    }
    function dfsA(node: number, from: number, income: number) {
        income += amount[node];
        if (from >= 0 && graph[node].length === 1) {
            return income;
        }
        let res = -Infinity;
        for (const child of graph[node]) {
            if (child === from) continue;
            res = Math.max(res, dfsA(child, node, income));
        }
        return res;
    }
    const graph = makeGraph();
    clearB(graph);
    return dfsA(0, -1, 0);
};

