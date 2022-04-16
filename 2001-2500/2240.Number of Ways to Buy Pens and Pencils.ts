function waysToBuyPensPencils(total: number, cost1: number, cost2: number): number {
    const c1 = Math.max(cost1, cost2);
    const c2 = Math.min(cost1, cost2);
    let res = 0;
    for (let remain = total; remain >= 0; remain -= c1) {
        res += Math.floor(remain / c2) + 1;
    }
    return res;
};

