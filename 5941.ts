function findAllPeople(n: number, meetings: number[][], firstPerson: number): number[] {
    meetings.sort((m1, m2) => m1[2] - m2[2]);
    const data = Array(n);
    function find(x: number, data) {
        if (data[x] === undefined) {
            data[x] = x;
        }
        if (data[x] !== x) {
            data[x] = find(data[x], data);
        }
        return data[x];
    }
    function union(x: number, y: number, data) {
        const rx = find(x, data);
        const ry = find(y, data);
        if (rx !== ry) {
            data[rx] = Math.min(rx, ry);
            data[ry] = Math.min(rx, ry);
        }
    }
    function unionBatch(i, j) {
        const group = {};
        for (let k = i; k < j; k++) {
            const [x, y, t] = meetings[k];
            union(x, y, group)
        }
        const knowHeads = new Set();
        for (let k = i; k < j; k++) {
            const [x, y, t] = meetings[k];
            if (0 === find(x, data) || 0 === find(y, data)) {
                knowHeads.add(find(x, group));
            }
        }
        for (let k = i; k < j; k++) {
            const [x, y, t] = meetings[k];
            if (knowHeads.has(find(x, group))) {
                union(0, x, data);
            }
            if (knowHeads.has(find(y, group))) {
                union(0, y, data);
            }
        }
    }
    union(0, firstPerson, data);
    for (let i = 0; i < meetings.length; i++) {
        let know = false;
        let j = i;
        while (j < meetings.length && meetings[i][2] === meetings[j][2]) {
            const [x, y, t] = meetings[j];
            know ||= 0 === find(x, data) || 0 === find(y, data);
            j++;
        }
        if (know) {
            unionBatch(i, j);
        }
        i = j - 1;
    }
    const res = [];
    for (let i = 0; i < n; i++) {
        if (0 === find(data[i], data)) {
            res.push(i);
        }
    }
    return res;
};

