function goodDaysToRobBank(security: number[], time: number): number[] {
    const n = security.length;
    security.push(Infinity);
    const prev = Array(n);
    prev[0] = 0;
    for (let i = 1; i < n; i++) {
        prev[i] = security[i] <= security[i - 1] ? prev[i - 1] + 1 : 0;
    }
    const res = [];
    let acc = -1;
    for (let i = n - 1; i >= time; i--) {
        acc = security[i] <= security[i + 1] ? acc + 1 : 0;
        if (acc >= time && prev[i] >= time) {
            res.push(i);
        }
    }
    return res;
};

