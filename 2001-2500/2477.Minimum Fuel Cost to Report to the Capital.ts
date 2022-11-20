function minimumFuelCost(roads: number[][], seats: number): number {
    const graph = {0 : []};
    for (const [u, v] of roads) {
        graph[u] ||= [];
        graph[u].push(v);
        graph[v] ||= [];
        graph[v].push(u);
    }
    // return [cur_cost, people_cnt]
    function dfs(node, from) {
        let cur_cost = 0, people_cnt = 1;
        for (const child of graph[node]) {
            if (child === from) continue;
            const rtn = dfs(child, node);
            cur_cost += rtn[0];
            people_cnt += rtn[1];
        }
        if (node !== 0) {
            cur_cost += Math.ceil(people_cnt / seats);
        }
        return [cur_cost, people_cnt];
    }
    return dfs(0, null)[0];
};

