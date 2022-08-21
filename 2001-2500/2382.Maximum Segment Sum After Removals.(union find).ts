function maximumSegmentSum(nums: number[], removeQueries: number[]): number[] {
    nums.unshift(0);
    nums.push(0);
    const data: number[] = Array.from(Array(nums.length).keys());
    const sum: number[] = Array(nums.length).fill(0);
    function find(x: number) {
        if (data[x] !== x) {
            data[x] = find(data[x]);
        }
        return data[x];
    }

    function union(x, y) {
        let xr = find(x);
        let yr = find(y);
        if (xr !== yr) {
            data[yr] = xr;
        }
    }
    const res = [0];
    for (const query of removeQueries.reverse()) {
        sum[query + 1] = nums[query + 1];
        const newSum = sum[find(query)] + sum[query + 1] + sum[find(query + 2)];
        if (sum[query]) union(query, query + 1);
        if (sum[query + 2]) union(query + 1, query + 2);
        sum[find(query + 1)] = newSum;
        res.push(Math.max(res[res.length - 1], newSum));
    }
    res.pop();
    return res.reverse();
};

