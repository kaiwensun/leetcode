function destroyTargets(nums: number[], space: number): number {
    const hash = {}, min = {};
    for (const num of nums) {
        const res = num % space;
        hash[res] ||= 0;
        hash[res]++;
        min[res] ||= Infinity;
        min[res] = Math.min(min[res], num);
    }
    let res = -1;
    hash[-1] = 0;
    for (const key of Object.keys(hash)) {
        if (hash[key] > hash[res] || (hash[key] === hash[res] && min[key] < min[res])) {
            res = parseInt(key);
        }
    }
    return min[res];
};

