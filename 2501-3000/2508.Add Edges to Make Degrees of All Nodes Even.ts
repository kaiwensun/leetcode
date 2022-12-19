/*
Don't forget the situation where a and b can use a third point c to achieve an even degree.
*/

function isPossible(n: number, edges: number[][]): boolean {
    const graph: {[key: number]: Set<number>} = {};
    for (const [u, v] of edges) {
        graph[u] ||= new Set<number>();
        graph[u].add(v);
        graph[v] ||= new Set<number>();
        graph[v].add(u);
    }
    const odds = Object.keys(graph).filter(u => graph[u].size % 2).map(odd => parseInt(odd));
    if (odds.length === 0) return true;
    if (odds.length === 2) {
        return !graph[odds[0]].has(odds[1]) || new Set([...graph[odds[0]], ...(graph[odds[1]])]).size != n;
    }
    if (odds.length === 4) {
        const [a, b, c, d] = odds;
        return !graph[a].has(b) && !graph[c].has(d) ||
            !graph[a].has(c) && !graph[b].has(d) ||
            !graph[a].has(d) && !graph[b].has(c);
    }
    return false;
};
