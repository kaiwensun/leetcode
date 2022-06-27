function countPairs(n: number, edges: number[][]): number {
    const data = new Array(n);
    for (let i = 0; i < n; i++) {
        data[i] = i;
    }
    function find(x: number) {
        if (data[x] !== x) {
            data[x] = find(data[x]);
        }
        return data[x];
    }
    function union(x: number, y: number) {
        const rx = find(x);
        const ry = find(y);
        if (rx !== ry) {
            data[rx] = ry;
        }
    }
    for (let [a, b] of edges) {
        union(a, b);
    }
    const counter: {[key: string]: number} = {};
    for (const r of data) {
        counter[find(r)] ||= 0;
        counter[find(r)]++;
    }
    let res = 0;
    for (let count of Object.values(counter)) {
        res += count * (n - count);
    }
    return res / 2;
};

