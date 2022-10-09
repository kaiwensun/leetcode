function findArray(pref: number[]): number[] {
    const res = [];
    let acc = 0;
    for (const target of pref) {
        const cur = target ^ acc;
        res.push(cur);
        acc ^= cur;
    }
    return res;
};

