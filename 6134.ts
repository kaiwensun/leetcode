function closestMeetingNode(edges: number[], node1: number, node2: number): number {
    function calcDist(node: number) {
        const dist = {};
        function dfs(node: number, acc: number) {
            if (dist[node] === undefined) {
                dist[node] = acc;
                if (edges[node] !== -1) {
                    dfs(edges[node], acc + 1);
                }
            }
        }
        dfs(node, 0);
        return dist;
    }
    const dist1 = calcDist(node1);
    const dist2 = calcDist(node2);
    const res = [Infinity, -1];
    for (const keyStr of Object.keys(dist1)) {
        const key = parseInt(keyStr);
        if (dist2[key] !== undefined) {
            const d = Math.max(dist1[key], dist2[key]);
            if (d < res[0] || (d === res[0] && key < res[1])) {
                res[0] = d;
                res[1] = key;
            }
        }
    }
    return res[1];
};

