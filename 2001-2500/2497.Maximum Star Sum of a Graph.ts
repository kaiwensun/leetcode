function maxStarSum(vals: number[], edges: number[][], k: number): number {
    function makeGraph(edges: number[][]) {
        const graph: {[key : number] : number[]} = {};
        edges.forEach(([u, v]) => {
            graph[u] ||= []; graph[u].push(v);
            graph[v] ||= []; graph[v].push(u);
        });
        return graph;
    }
    function getStarSum(center: number) {
        const neighbors = graph[center] || [];
        neighbors.sort((a, b) => vals[b] - vals[a]);
        let res = vals[center];
        for (const neighbor of neighbors.slice(0, k)) {
            if (vals[neighbor] <= 0) break;
            res += vals[neighbor];
        }
        return res;
    }
    const graph = makeGraph(edges);
    return vals.reduce((acc, _, center) => Math.max(acc, getStarSum(center)), -Infinity);
};

