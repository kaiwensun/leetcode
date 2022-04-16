function maximumScore(scores: number[], edges: number[][]): number {
    function addHighestNeighbor(u, v) {
        highestNeighbors[u] ||= [[-Infinity, -1]];
        for (let i = 0; i < highestNeighbors[u].length; i++) {
            if (scores[v] > highestNeighbors[u][i][0]) {
                highestNeighbors[u].splice(i, 0, [scores[v], v]);
                break;
            }
        }
        if (highestNeighbors[u].length > 3) {
            highestNeighbors[u].pop();
        }
    }
    function getMaxSequenceScore(u, v) {
        const uarr = highestNeighbors[u].filter(pair => pair[1] !== v);
        const varr = highestNeighbors[v].filter(pair => pair[1] !== u);
        if (Math.min(uarr.length, varr.length) < 2) {
            return -1;
        }
        if (uarr[0][1] !== varr[0][1]) {
            return scores[u] + scores[v] + uarr[0][0] + varr[0][0];
        } else {
            return scores[u] + scores[v] + Math.max(uarr[1][0] + varr[0][0], uarr[0][0] + varr[1][0]);
        }
    }

    const highestNeighbors = {};
    for (const [u, v] of edges) {
        addHighestNeighbor(u, v);
        addHighestNeighbor(v, u);
    }
    return edges.reduce((res, [u, v]) => Math.max(res, getMaxSequenceScore(u, v)), -1);
};

