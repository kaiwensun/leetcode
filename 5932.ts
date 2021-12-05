function validArrangement(pairs: number[][]): number[][] {
    const graph: {[key: number]: number[][]} = {};
    const count: {[key: number]: number} = {};
    for (let pair of pairs) {
        const [start, end] = pair;
        graph[start] ||= [];
        graph[start].push(pair);
        count[start] ||= 0;
        count[start]++;
        count[end] ||= 0;
        count[end]--;
    }
    let start = undefined;
    for (const [key, value] of Object.entries(count)) {
        if (value == 1) {
            start = key;
            break;
        }
        start = key;
    }
    const result = [];
    function dfs(start) {
        while (graph[start]?.length) {
            let pair = graph[start].pop();
            dfs(pair[1]);
            result.push(pair);
        }
    }
    dfs(start);
    return result.reverse();
};

