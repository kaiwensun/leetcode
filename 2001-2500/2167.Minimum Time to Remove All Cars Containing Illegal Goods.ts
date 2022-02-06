function minimumTime(s: string): number {
    function getWorthwhileArray(s) {
        const res = [-1];
        let prevInd = -1, cnt = 0;
        for (let i = 0; i < s.length; i++) {
            if (s[i]) {
                cnt++;
                if (cnt * 2 >= i - prevInd) {
                    res.push(i);
                    prevInd = i;
                    cnt = 0;
                }
            }
        }
        return res;
    }

    const N = s.length;
    const arr = [...s].map(e => parseInt(e));
    const total = arr.filter(e => e).length;
    if (total === 0) {
        return 0;
    }
    const left = getWorthwhileArray(arr);
    const right = getWorthwhileArray(arr.slice().reverse()).map(i => N - 1 - i).reverse();

    const prefix = [0];
    for (let i = 0; i < N; i++) {
        prefix.push(prefix[i] + arr[i]);
    }

    function rangeSum(start: number, end: number) {
        if (end <= start) return 0;
        return prefix[end] - prefix[start];
    }

    let rIter = 0, res = Infinity;
    for (const l of left) {
        while (rIter < right.length && right[rIter] <= l) {
            rIter++;
        }
        const r = right[rIter];
        const leftCost = l + 1;
        const rightCost = N - r;
        const midCost = rangeSum(l + 1, r) * 2;
        res = Math.min(res, leftCost + midCost + rightCost);
    }
    return res;
};

