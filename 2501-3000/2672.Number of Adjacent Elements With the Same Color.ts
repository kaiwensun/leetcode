function colorTheArray(n: number, queries: number[][]): number[] {
    const config = {};
    const res = [];
    let same = 0;
    queries.forEach(([i, color]) => {
        if (config[i] !== color) {
            if (config[i]) {
                [-1, 1].forEach(diff => same -= config[i + diff] == config[i] ? 1 : 0);
            }
            config[i] = color;
            [-1, 1].forEach(diff => same += config[i + diff] == config[i] ? 1 : 0);
        }
        res.push(same);
    });
    return res;
};


